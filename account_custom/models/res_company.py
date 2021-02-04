# -*- coding: utf-8 -*-

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    logo_2 = fields.Binary(string='Company Logo 2', attachment=True)