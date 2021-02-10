# -*- coding: utf-8 -*-
{
    'name': "Custom picking report",

    'summary': """
        Customised picking report""",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base','stock'],
    'data': [
        'views/custom_picking_report.xml',
    ],
    'installable': True,
    'application': True,
}
