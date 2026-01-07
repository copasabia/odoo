# -*- coding: utf-8 -*-
{
    'name': 'Copasabia Navigation',
    'version': '1.0',
    'category': 'Custom',
    'description': 'Adds navigation button to Copasabia almacen-beta from Odoo',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'copasabia_navigation/static/src/navbar_patch.js',
            'copasabia_navigation/static/src/navbar_patch.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
