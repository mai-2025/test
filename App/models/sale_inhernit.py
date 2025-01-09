from odoo import fields, models, api


class SaleInhernit(models.Model):
    _inherit = ["sale.order"]
    book_id = fields.Many2one('book.book')


