from odoo import fields, models, api


class SaleCurrency(models.Model):
    _description = 'Description'
    _inherit ='student'
    _name = 'student.payment'
    _order = 'code_id'

    st_name = fields.Char(required=True)
    st_pay_id=fields.Many2one('student')
    code_id=fields.Char(related='st_pay_id.st_code')
    tax=fields.Float()
    currency_id_rate=fields.Many2one('res.currency')
    rate = fields.Float(related='currency_id_rate.rounding')
    total_fees=fields.Float(compute='_compute_total_currency_rate')

    @api.depends('currency_id_rate','rate')
    def _compute_total_currency_rate(self):
           for rec in self:
               if rec.currency_id_rate:
                  print(rec.rate)
                  rec.total_fees=rec.tax*rec.rate
               else:
                   rec.total_fees==0
