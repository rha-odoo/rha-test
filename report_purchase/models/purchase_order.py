# Copyright YEAR(S), AUTHOR(S)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    ship_via = fields.Selection([('air_freight', 'Air Freight'), ('sea_freight', 'Sea Freight'), ('road_freight', 'Road Freight')], string="Ship Via")