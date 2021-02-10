# -*- coding: utf-8 -*-
{
    'name': "Sale Order Report Customization",

    'summary': """
        Modified the sale order report.""",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'application': True,
}
