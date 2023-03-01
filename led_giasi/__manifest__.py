# -*- coding: utf-8 -*-
{
    'name': 'Led Gia Si',
    'version': '1',
    'category': 'Led Gia Si',
    'live_test_url': '#',
    'summary': 'Phần mềm quản lý',
    'author': 'Lv Quy',
    'company': '',
    'website': 'https://#',
    'depends': ['base_setup','website'],
    'data': [
        #data
        # report
        # views
        'views/custom_footer.xml'
    ],

    'assets': {
        'web.assets_backend': [

        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
}
