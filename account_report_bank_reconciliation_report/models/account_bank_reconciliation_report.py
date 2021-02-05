# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.tools.misc import formatLang, format_date
# from odoo.osv import expression

class account_bank_reconciliation_report(models.AbstractModel):
    _inherit = 'account.bank.reconciliation.report'

    @api.model
    def _get_payment_report_lines(self, options, journal):
        rslt = super(account_bank_reconciliation_report, self)._get_payment_report_lines(options, journal)
        journal_id = self._context.get('active_id') or options.get('active_id')
        # Bank statement lines reconciled with a payment
        for i in rslt[0]: 
            i['reconciled_st_positive'] = self.env['account.bank.statement.line'].search([('statement_id.journal_id', '=', journal_id),
                                                                                 ('date', '<=', options['date']['date_to']),
                                                                                 ('line_ids', '!=', False),
                                                                                 ('amount', '>', 0)])

            i['reconciled_st_negative'] = self.env['account.bank.statement.line'].search([('statement_id.journal_id', '=', journal_id),
                                                                                 ('date', '<=', options['date']['date_to']),
                                                                                 ('line_ids', '!=', False),
                                                                                 ('amount', '<', 0)])
            break
        return rslt

    def _add_bank_statement_line(self, line, amount):
        name = line.payment_ref
        line_currency = self.env.context.get('line_currency', False)
        return {
            'id': str(line.id),
            'caret_options': 'account.bank.statement',
            'model': 'account.bank.statement.line',
            'name': len(name) >= 75 and name[0:70] + '...' or name,
            'columns': [
                {'name': format_date(self.env, line.date), 'class': 'date'},
                {'name': line.ref},
                {'name': self.format_value(amount, line_currency)},
            ],
            'class': 'o_account_reports_totals_below_sections',
        }
    #line_number = 0
    def _add_title_line(self, options, title, amount=None, level=0, date=False):
        # self.line_number += 1
        line_currency = self.env.context.get('line_currency', False)
        return {
            'id': 'line_',
            'name': title,
            'columns': [
                {'name': date and format_date(self.env, date) or '', 'class': 'date'},
                {'name': ''},
                {'name': amount and self.format_value(amount, line_currency)},
            ],
            'level': level,
        }

    @api.model
    def _get_lines(self, options, line_id=None):
        lines = super(account_bank_reconciliation_report, self)._get_lines(options, line_id)
        # Fetch data
        journal = self.env['account.journal'].browse(options['active_id'])
        report_data = self._get_payment_report_lines( options, journal)

        for bda in report_data[0]:
            if bda.get('reconciled_st_positive') or bda.get('reconciled_st_negative'):
                counter = 3
                lines.insert(counter, self._add_title_line(options, _("Reconciled Bank Statement Lines"), level=2))
                for line in bda.get('reconciled_st_positive'):
                    counter += 1
                    lines.insert(counter, self._add_bank_statement_line(line, line.amount))
                for line in bda.get('reconciled_st_negative'):
                    counter += 1
                    lines.insert(counter, self._add_bank_statement_line(line, line.amount))
        return lines