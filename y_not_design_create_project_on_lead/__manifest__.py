# -*- coding: utf-8 -*-
{
    'name': "Create Project on lead",

    'summary': """
        Create project from project template on Opportunity many products""",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base', 'base_automation', 'crm', 'project'],
    'data': [
        'views/base_automation.xml',
    ],
    'installable': True,
    'application': True,
}
