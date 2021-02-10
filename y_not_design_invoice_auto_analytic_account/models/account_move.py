from odoo import models, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.onchange('product_id')
    def _compute_account_analytic_id(self):
        if self.product_id and self.product_id.product_tmpl_id:
            analytic_account_id = self.env['account.analytic.account'].search(
                [('x_studio_product', '=', self.product_id.product_tmpl_id.id)], limit=1)
            if analytic_account_id:
                self.analytic_account_id = analytic_account_id.id

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('analytic_account_id'):
                product_tmpl_id = self.env['product.product'].browse(vals['product_id']).product_tmpl_id
                if vals.get('product_id') and product_tmpl_id:
                    analytic_account_id = self.env['account.analytic.account'].search([('x_studio_product', '=', product_tmpl_id.id)], limit=1)
                    if analytic_account_id:
                        vals['analytic_account_id'] = analytic_account_id.id
        return super(AccountMoveLine, self).create(vals_list)
