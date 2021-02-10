# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # -----------------------
    # Action method
    # ----------------------
    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        
        # Search only one matched record (limit =1)
        picking_type_id = self.env['stock.picking.type'].search([('operation_receipt', '=', True)], limit=1)
        
        # generate the duplicate receipt and add into vendor operation type (inventory).
        picking_id = self.picking_ids.filtered(lambda picking: picking.picking_type_id.code == 'incoming')
        if picking_id:
            internal_picking = picking_id.copy({
                'picking_type_id': picking_type_id.id,
                'internal_purchase_order': self.id,
                'location_id': picking_type_id.default_location_src_id.id,
                'location_dest_id': picking_type_id.default_location_dest_id.id,
            })
            internal_picking.move_lines.write({'group_id': False, 'purchase_line_id': False, 'picking_type_id': internal_picking.picking_type_id.id})
        return res
