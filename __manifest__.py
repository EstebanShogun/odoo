# -*- coding: utf-8 -*-
{
    'name': "projet",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "esteban",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/tdsimodel_security.xml',
        'datas/datas.xml',
        'views/views.xml',
        'views/viewBrand.xml',
        'views/viewProf.xml',
        'views/viewEleve.xml',
        'views/viewClasse.xml',
        'views/viewCours.xml',
        'iutmodel_menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
