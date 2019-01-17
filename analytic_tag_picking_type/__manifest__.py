# -*- coding: utf-8 -*-

{
    'name': 'Analytic Tag - Stock Picking',
    'version': '10.0.1.0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Add analytic tags to stock pickings, to pass onto purchases.',
    'author': 'Mark Robinson, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'depends': ['account', 'purchase', 'stock'],
    'data': [
        'views/stock_picking_type.xml'
    ],
    'installable': True,
}
