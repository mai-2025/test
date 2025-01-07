
from odoo import models,fields,api
from odoo.exceptions import UserError ,ValidationError

class LIB(models.Model):
    _name ='book.book'
    _description = "Book"
    name=fields.Char()
    book_code=fields.Integer()
    due_date=fields.Date()
    active =fields.Boolean(default=True)
    student_id=fields.Many2one('student')
    category_ids = fields.Many2many(
        'hr.employee.category', 'employee_category_rel_rel',
        'emp_id', 'category_id',
        string='Tags')
    level_ids = fields.Many2many(
        'student', 'student_category_rel',
        'st_id', 'category_id',
        string='Tags')
    price_book=fields.Float()

    _sql_constraints = [('constraint_code_unique','unique(book_code)','The code mustbe unique')]


    @api.constrains('price_book')
    def _check_total_fees(self):
        print(self)
        for rec in self:
          if rec.price_book < 0.0:
            print(rec.name)
            raise ValidationError("Please inter positive value")
