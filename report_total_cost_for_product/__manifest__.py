# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Total Product Cost Report',
    'category': 'customisation',
    'summary': 'Report',
    'depends': [
        'account_accountant',
        'account_custom',
        'mrp',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_total_product_cost_view.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
