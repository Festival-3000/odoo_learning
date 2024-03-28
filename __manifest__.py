# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Employee Management System',
    'version' : '15',
    'summary': 'Employee Management System',
    'sequence': 10,
    'description': """
Employee Management System
====================
    """,
    'category': 'Management/Employee',
    'website': 'https://www.botspotinfoware.com/',
    'depends' : ['base'],
    'data': [
        # 'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/client_views.xml',
        'views/project_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}