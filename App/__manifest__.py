{
    'name': 'App1',
    'version': '1.0',
    'summary': 'Summery',
    'description': 'Description',
    'category': 'Accounting/Accounting',
    'author': 'Author',
    'website': 'website',
    #'license': 'License',
    'depends': ['base_setup','hr','sale'],
    'data': [
       'security/ir.model.access.csv',
       'security/library_view_group.xml',
       'views/menu_book.xml',
       'views/book.xml',
       'views/studnt_view.xml',
       #'views/student_payment_view.xml',
             ],
    'demo': ['Demo'],
    'installable': True,
    'auto_install': False
}