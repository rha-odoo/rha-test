# -*- coding: utf-8 -*-
{
    'name': "Sale Customisation",
    'summary': """Customisation Of Sale""",
    'description': """
        -- Change the Print button name for base on order type.
        -- Price validation on unit price.
    """,
    'author': "Odoo",
    'website': "http://www.odoo.com",
    'category': 'Customisation',
    'version': '0.1',
    'depends': [
        'product',
        'sale',
        'sale_management'
    ],
    'data': [
        "views/view_sale_order.xml",
    ],
    'demo': [

    ],
}
