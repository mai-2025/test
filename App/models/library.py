
from odoo import models,fields,api
#from odoo.exceptions import UserError ,ValidationError
class LIB(models.Model):
    _name ='book.book'
    name=fields.Char()
    book_code=fields.Integer()
    due_date=fields.Date()
    active =fields.Boolean(default=True)
    student_id=fields.Many2one('student')
    category_ids = fields.Many2many(
        'hr.employee.category', 'employee_category_rel_rel',
        'emp_id', 'category_id',
        string='Tags')









   #  _sql_constraints = [('constraint_code_unique','unique(code)','The code mustbe unique')]


""""@api.constrains('fees_total')
def _check_total_fees(self):
    for i in self:
        if i.fees_total < 0.0:
            print(i)
            raise ValidationError("Please inter positive value")"""