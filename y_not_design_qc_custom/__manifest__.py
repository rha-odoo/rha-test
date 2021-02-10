# -*- coding: utf-8 -*-
{
    'name': 'Quality Control Customization',
    'version': '12.0.1.0',
    'category': '',
    'description': u"""
- Added new menu and added some custom fields in quality controls.
""",
    'author': '',
    'depends': [
        'project',
        'quality',
        'quality_control',
    ],
    'data': [
        'data/model_factory_audit.xml',
        'data/fields_quality_alerts.xml',
        'data/fields_factory_audit.xml',
        'security/ir.model.access.csv',
        'views/view_res_partner.xml',
        'views/quality_alerts_tasks_view.xml',
        'views/quality_factory_audit.xml',
        'views/quality_control_tasks_view.xml',
    ],
    'application': False,
}
