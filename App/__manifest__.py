{
    'name': 'App1',
    'version': '1.0',
    'summary': 'Summery',
    'description': 'Description',
    'category': 'Accounting/Accounting',
    'author': 'Author',
    'website': 'website',
    #'license': 'License',
    'depends': ['base_setup','hr','sale','web'],
    'data': [
       'security/ir.model.access.csv',
       'security/library_view_group.xml',
       'views/menu_book.xml',
       'views/book.xml',
       'views/studnt_view.xml',
       'views/student_payment_view.xml',
       'data/book_return_date.cron.xml',
        'wizard/report_wizard.xml',
        'report/student_report.xml',
        'report/report_wizard_template.xml',
             ],
    'demo': ['Demo'],
    'installable': True,
    'auto_install': False
}