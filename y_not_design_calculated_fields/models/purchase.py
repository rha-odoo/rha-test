from odoo import fields, models, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    x_balance_qty = fields.Float(string='Balance Qty', compute='_compute_x_balance_qty', store=True)

    @api.depends('product_qty', 'qty_received')
    def _compute_x_balance_qty(self):
        for record in self:
            record['x_balance_qty'] = record.product_qty - record.qty_received
