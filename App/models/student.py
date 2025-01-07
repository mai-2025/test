from odoo import models,fields,api


class Student(models.Model):
     _name='student'
     st_name=fields.Char(required=True)
     book_ids=fields.One2many('book.book','student_id')
     active_name =fields.Boolean(default=False)
     st_code=fields.Char(compute='_compute_st_code' ,copy=False)

     def _compute_st_code(self):
          for record in self:
               #if not record.st_code:
               record.st_code = self.env['ir.sequence'].next_by_code('st_code')