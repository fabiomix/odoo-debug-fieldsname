# -*- coding: utf-8 -*-
{
    'name': 'Debug Fields Name',
    'summary': 'Show fields name in views',
    'description': '''
        Replace fields label with fields name in views (for development purposes).
    ''',

    'author': 'fabiomix',
    'website': '',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '10.0.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        'security/res_groups.xml'
    ],

    'application': False,
    'installable': True
}
