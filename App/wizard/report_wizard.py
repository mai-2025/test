from odoo import models, fields, api
import io
import xlsxwriter
from odoo import http
from odoo.http import request

# Wizard Model
class ReportFromWizard(models.TransientModel):
    _name = "report.wizard"
    report_type=fields.Selection(selection=[('pdf_report','Pdf Report'),('xlxs_report','XLXS Report ')])
    company_id = fields.Many2one('res.company' , string='Collage')
    partner_id = fields.Many2one('res.partner',string="Customer")

    def print_report(self):

        lib_ids = self.env['student'].search([('company_id', '=', self.company_id.id)])
        print(lib_ids)
        #for rec in lib_ids:
        return self.env.ref("App.report_1_id").report_action(lib_ids)


    def action_close(self):
        return {'type': 'ir.actions.act_window_close'}



    def print_report_xls(self):
         return {
              'type' :'ir.actions.act_url',
               'url': '/report/lib/download?partner_id=%s' % self.partner_id.id,
               'target':'new'
              }
# HTTP Controller for XLSX Export
class ReportXLSx(http.Controller):
    #Cross-Site Request Forgery
    @http.route('/report/lib/download', type='http', auth='public', csrf=False)
    def export_xls(self,partner_id):
        print(partner_id)
        partner = request.env['res.partner'].browse(int(partner_id))
        # Initialize the in-memory binary stream
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Report LIB')
        # Define headers
        headers = ['NAME' ,'phone']
        for col, head in enumerate(headers):
            sheet.write(0, col, head)
        row = 1
        sheet.write(row,0, partner.name)
        sheet.write(row,1, partner.phone)
        row+=1
        # Close the workbook
        workbook.close()
        output.seek(0)

        # Return the XLSX file as an HTTP response
        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'inline; filename="partner_report.xlsx"')
            ]
        )
