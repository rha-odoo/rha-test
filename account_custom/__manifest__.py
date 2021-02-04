# -*- coding: utf-8 -*-
{
    'name': "Custom invoice report",

    'summary': """
        Customised invoice report""",

    'category': 'Uncategorized',
    'version': '14.0',

    'depends': ['base','account_accountant','sale_management'],
    'data': [
        'views/view_res_company.xml',
        'views/view_account_invoice.xml',
        'report/custom_invoice_report.xml',
    ],
    'installable': True,
    'application': True,
}
