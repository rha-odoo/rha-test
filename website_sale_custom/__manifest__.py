# -*- coding: utf-8 -*-
{
    'name': "Website Sale Customisation",
    'summary': """Customisation Of Sale""",
    'description': """
        -- Q & A Display in shop page at last.
    """,
    'author': "Odoo",
    'website': "http://www.odoo.com",
    'category': 'Customisation',
    'version': '0.1',
    'depends': [
        'product',
        'sale',
        'sale_management',
        'website_sale',
    ],
    'data': [
        "views/website_sale_templates.xml",
    ],
    'demo': [

    ],
}
