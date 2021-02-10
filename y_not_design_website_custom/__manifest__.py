# -*- coding: utf-8 -*-
{
    'name' : 'Website Customization',
    'version' : '1.1',
    'summary': 'Customization',
    'sequence': 200,
    'description': """
- Added custom tax exemption on webiste my home file attachment.
- Added custom field tax exemption on contact.
- Max Qty on website add to cart (shop) page.
- Do not allow more than qty for maximum qty on product (max qty are on hand qty - outgoing qty).
- Display Sign up button instead of 'Process Checkout' on website if customer is not logged.
    """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : [
        'base_import_module',
        'contacts',
        'portal',
        'website',
        'website_sale',
        'website_sale_stock',
    ],
    'data': [
    	# 'data/partner_fields.xml',
    	'data/website_server_action.xml',
    	'views/res_partner_view.xml',
    	'views/website_templates.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
