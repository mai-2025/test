
from odoo import models,fields,api

class Student(models.Model):
     _name='student'
     st_name=fields.Char()
     st_code=fields.Integer(required=True)
     book_ids=fields.One2many('book.book','student_id')
