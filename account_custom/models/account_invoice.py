# -*- coding: utf-8 -*-

from odoo import fields, models, api

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    is_cruise_lines = fields.Boolean(string='Is Cruise Lines')

class AccountAccount(models.Model):
    _inherit = 'account.account'

    is_interim = fields.Boolean(string='Is Interim')

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    sales_qty = fields.Float('Sales Qty', compute="_compute_sales_qty", store=True)

    @api.depends('account_id', 'quantity')
    def _compute_sales_qty(self):
        for line in self:
            if line.account_internal_group == 'income':
                line.sales_qty = line.quantity