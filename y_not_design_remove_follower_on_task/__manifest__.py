# -*- coding: utf-8 -*-
{
    'name': "Remove Follower on Task",

    'summary': """
        Remove Follower on Task when duplicate the project with task.""",

    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base', 'base_automation', 'crm', 'project'],
    'data': [
        'views/view_project_project.xml',
    ],
    'installable': True,
    'application': True,
}
