# -*- coding: utf-8 -*-
{
    'name': "rw_security_website",

    'summary': """
        Restrict permission for public users""",

    'description': """
        This will allow internal users to view company blogs 
    """,

    'author': "Rulesware LLC",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','website_blog','website_forum'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
