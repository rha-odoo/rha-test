# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Purchase Report Customisation',
    'category': 'customisation',
    'summary': 'Purchase Report',
    'depends': [
        'purchase',
    ],
    'data': [
        'views/view_purchase_order.xml',
        'views/report_purchaseorder_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
