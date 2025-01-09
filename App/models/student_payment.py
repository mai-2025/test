from odoo import fields, models, api
from odoo.addons.test_impex.models import selection_fn


class SaleCurrency(models.Model):
    _description = 'StudentPayment'
    _inherit ='student'
    _name = 'student.payment'
    _order = 'code_id'
    _inherits = {'book.book': 'book_id'}

    st_pay_id=fields.Many2one('student')
    code_id=fields.Char(related='st_pay_id.st_code')
    tax=fields.Float()
    currency_id_rate=fields.Many2one('res.currency')
    rate = fields.Float(related='currency_id_rate.rounding')
    total_fees=fields.Float(compute='_compute_total_currency_rate')
    book_id=fields.Many2one('book.book')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
        ],
        default='draft',
        string="Status"
    )




    @api.depends('currency_id_rate','rate')
    def _compute_total_currency_rate(self):
           for rec in self:
               if rec.currency_id_rate:
                  rec.total_fees=rec.tax*rec.rate
               else:
                   rec.total_fees==0

    def create_student_payment(self):
        for rec in self:
            student_payment = self.env['account.payment'].create({
                'ref': rec.st_pay_id.st_name,  # Use 'rec' to refer to the current record in the loop
                'amount': rec.total_fees,
                'state':'posted',
            })
            print(f"Payment created for: {rec.st_pay_id.st_name}, Amount: {rec.total_fees}")

    def confirm(self):
        if self.state=='draft':
            self.write(({'state':'confirm'}))
