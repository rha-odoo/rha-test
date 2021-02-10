from odoo import fields, models, api


class SalesOrder(models.Model):
    _inherit = 'sale.order'

    x_open_balance = fields.Monetary(string='Open balance', compute='_compute_x_open_balance', store=True)

    @api.depends('order_line.price_subtotal', 'order_line.untaxed_amount_invoiced')
    def _compute_x_open_balance(self):
        for record in self:
            open_balance = 0
            for line in record.order_line:
                open_balance += (line.price_subtotal - line.untaxed_amount_invoiced)
            record.update({'x_open_balance': open_balance})
