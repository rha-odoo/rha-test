# -*- coding: utf-8 -*-
{
    'name': "Compute open balance in sale order and balance quantity in purchase order line",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'sale_management', 'purchase'],
    'data': [
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': True,
}
