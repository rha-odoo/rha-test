# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import Warning


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('price_unit')
    def _onchange_price_unit(self):
        price_unit = round(self.price_unit, 4)
        if price_unit and price_unit > 1:
            dp = str(price_unit).split(".")[1]
            if len(dp) > 2:
                raise Warning("Price can not be more than 2 precision value")

        if price_unit and price_unit < 1:
            dp = str(price_unit).split(".")[1]
            if len(dp) > 3:
                raise Warning("Price can not be more than 3 precision value")
