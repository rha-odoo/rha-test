# Copyright YEAR(S), AUTHOR(S)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_tax_exemption_file = fields.Binary(string='Tax Exemption File', attachment=True)
    x_tax_exemption_filename = fields.Char(string='Tax Exemption File Name')