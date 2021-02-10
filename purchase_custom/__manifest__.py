# -*- coding: utf-8 -*-
{
    'name': "Purchase Custom",
    'summary': """Picking Receipt Copy""",
    'author': "Odoo India",
    'description': """
        When Purchase Order Confirm Create once Picking Receipt copy into internal transfer.
    """,
    'website': "http://www.odoo.com",
    'category': 'Customisation',
    'version': '0.1',
    'depends': [
        'base',
        'purchase',
        'stock',
    ],
    'data': [
        'views/view_stock_picking.xml',
    ],
}