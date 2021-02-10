# Copyright YEAR(S), AUTHOR(S)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('purchase_price', 'x_studio_margin')
    def _onchange_purchase_price_margin(self):
        self.price_unit = self.purchase_price / (1 - self.x_studio_margin / 100)