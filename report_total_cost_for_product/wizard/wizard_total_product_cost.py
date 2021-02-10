# -*- coding: utf-8 -*-

import io
# import xlwt
import base64
import datetime

from odoo import fields, models, api
from odoo.tools.misc import xlwt

class WizardProductCostReport(models.Model):
    _name = 'wizard.product.total.cost'
    _description = 'Total Cost For Product'

    product_ids = fields.Many2many('product.product', string="Products")
    datas = fields.Binary(string='Datas')
    datas_fname = fields.Char(string='File Name')

    def print(self):
        aml_lines = self.env['account.move.line'].search([])
    
        if self.product_ids:
            product_ids = self.product_ids
        else:
            product_ids = aml_lines.mapped('product_id')

        # Direct Cost contain user type name contain 'Cost of Revenue and Current Asset'
        # Filter user type entries in journal items.
        user_type_ids = self.env['account.account'].search(['|', ('user_type_id', 'ilike', 'Cost of Revenue'), ('user_type_id', 'ilike', 'Current Asset')])
        direct_cost_aml_lines = aml_lines.search(["&", ("account_id","in", user_type_ids.ids), ("account_id.is_interim","=", False), ('journal_id.type', '!=', "sale")])
        
        # Filter for Journal Entries which is created by unbuild model.
        unbuild_stock_move = self.env['stock.move'].search([('unbuild_id', '!=', False)])
        account_move = direct_cost_aml_lines.mapped('move_id').filtered(lambda move: move.stock_move_id.id in unbuild_stock_move.ids)
        
        if account_move:
            move_line_ids = account_move.mapped('line_ids')
            direct_cost_aml_lines = direct_cost_aml_lines.filtered(lambda aml: aml.id not in move_line_ids.ids)
        
        product_direct_cost_aml_lines = direct_cost_aml_lines.filtered(lambda aml: aml.product_id.id in product_ids.ids).filtered(lambda aml: aml.debit > 0)
        direct_cost_aml_lines = direct_cost_aml_lines.filtered(lambda aml: not aml.product_id and (aml.analytic_account_id and aml.analytic_account_id.x_studio_product.id in product_ids.mapped('product_tmpl_id').ids))
        direct_cost_aml_lines = direct_cost_aml_lines + product_direct_cost_aml_lines
        
        # Indirect Cost
        indirect_cost_aml_lines = aml_lines.search([("account_id","ilike","Expense")])
        indirect_cost_aml_lines = indirect_cost_aml_lines.filtered(lambda aml: aml.analytic_account_id and aml.analytic_account_id.x_studio_product.id in product_ids.mapped('product_tmpl_id').ids)

        # Define style for cells
        base_style = xlwt.easyxf('align: wrap yes')
        bold_style = xlwt.easyxf('font: bold 1')
        date_style = xlwt.easyxf('align: wrap yes', num_format_str='YYYY-MM-DD')

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Sheet 1')
        
        rows = [['Date', 'Journal Entry', 'Journal', 'Label', 'Reference', 'Partner', 'Account', 'Analytical Account', 'Cost']]
        
        row_index = 0
        
        product_name = ', '.join(map(lambda name: name, product_ids.mapped('name')))
        worksheet.write_merge(row_index, row_index, 0, 8, product_name, bold_style)

        row_index += 1
        default_codes = "Customer Reference: "
        default_codes += ', '.join(map(lambda name: name, product_ids.filtered(lambda x: x.default_code).mapped('default_code')))
        worksheet.write_merge(row_index, row_index, 0, 8, default_codes, bold_style)

        row_index += 1
        y_not_references = "Y Not Reference: "
        y_not_references += ', '.join(map(lambda name: name, product_ids.filtered(lambda x: x.x_studio_y_not_reference).mapped('x_studio_y_not_reference')))
        worksheet.write_merge(row_index, row_index, 0, 8, y_not_references, bold_style)

        # Direct cost lines
        row_index += 1
        worksheet.write_merge(row_index, row_index, 0, 7, "Direct Cost", bold_style)
        row_index += 1

        for row in rows:
            cell_index = 0
            for cell_value in row:
                cell_style = base_style
                worksheet.write(row_index, cell_index, cell_value, cell_style)
                cell_index += 1
            row_index += 1
        
        for aml_line in direct_cost_aml_lines:
            cell_index = 0
            res = [aml_line.date, aml_line.move_id.name, aml_line.journal_id.name, aml_line.name, aml_line.ref, aml_line.partner_id.display_name, aml_line.account_id.name, aml_line.analytic_account_id.name, (aml_line.debit - aml_line.credit)]
            for cell_value in res:
                cell_style = base_style
                if isinstance(cell_value, datetime.date):
                    cell_style = date_style 

                worksheet.write(row_index, cell_index, cell_value, cell_style)
                cell_index += 1
            row_index += 1

        direct_total_cost = sum(direct_cost_aml_lines.mapped('debit')) - sum(direct_cost_aml_lines.mapped('credit'))
        worksheet.write_merge(row_index, row_index, 0, 7, "Total Direct Cost", bold_style)
        row_index += 1
        worksheet.write_merge(row_index, row_index, 8, 8, direct_total_cost, bold_style)
        row_index += 1

        # Indirect cost lines
        worksheet.write_merge(row_index, row_index, 0, 7, "Indirect Cost", bold_style)
        row_index += 1
        for row in rows:
            cell_index = 0
            for cell_value in row:
                cell_style = base_style
                worksheet.write(row_index, cell_index, cell_value, cell_style)
                cell_index += 1
            row_index += 1
        
        for aml_line in indirect_cost_aml_lines:
            cell_index = 0
            res = [aml_line.date, aml_line.move_id.name, aml_line.journal_id.name, aml_line.name, aml_line.ref, aml_line.partner_id.display_name, aml_line.account_id.name, aml_line.analytic_account_id.name, (aml_line.debit - aml_line.credit)]
            for cell_value in res:
                cell_style = base_style
                if isinstance(cell_value, datetime.date):
                    cell_style = date_style 

                worksheet.write(row_index, cell_index, cell_value, cell_style)
                cell_index += 1
            row_index += 1
        
        indirect_total_cost =  sum(indirect_cost_aml_lines.mapped('debit')) - sum(indirect_cost_aml_lines.mapped('credit'))
        worksheet.write_merge(row_index, row_index, 0, 7, "Total Indirect Cost", bold_style)
        worksheet.write_merge(row_index, row_index, 8, 8, indirect_total_cost, bold_style)

        row_index += 1

        total_cost = direct_total_cost + indirect_total_cost
        worksheet.write_merge(row_index, row_index, 0, 7, "Total Cost", bold_style)
        worksheet.write_merge(row_index, row_index, 8, 8, total_cost, base_style)

        filename = ('Total Cost Report' + '.xls')
        workbook.save(filename)
        fp = open(filename, "rb")
        file_data = fp.read()
        self.datas = base64.encodebytes(file_data)
        fp.close()
        self.datas_fname = filename
        wizard = self.env.ref('report_total_cost_for_product.action_wizard_total_product_cost').read()[0]
        wizard['res_id'] = self.id
        return wizard