# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Orbyo analytics',
    'category': 'customisation',
    'summary': 'Orbyo analytics added script in website pages for google tag manager.',
    'version': '14.0',
    'depends': [
        'web',
        'website',
    ],
    'data': [
        'views/website_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
