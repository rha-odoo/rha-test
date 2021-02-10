# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # --------------------------
    # Fields Declaration
    # --------------------------
    internal_purchase_order = fields.Many2one('purchase.order', string='Purchase Order')


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    # --------------------------
    # Fields Declaration
    # --------------------------
    operation_receipt = fields.Boolean( string='Receipt Copy', default=False)