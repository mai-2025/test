from odoo import models, fields, api
import io
import xlsxwriter
from odoo import http
from odoo.http import request

# Wizard Model
class ReportFromWizard(models.TransientModel):
    _name = "report.wizard"

    company_id = fields.Many2one('res.company' , string='Collage')

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
              'url':f'/report/lib/download?wizard_id={self.id}',
              'target':'new'
              }
# HTTP Controller for XLSX Export
class ReportXLSx(http.Controller):
    @http.route('/report/lib/download', type='http', auth='public', csrf=False)
    def export_xls(self,wizard_id):
        print(wizard_id)
        wizard = request.env['report.wizard'].browse(int(wizard_id))
        partner_ids = wizard.partner_id
        # Initialize the in-memory binary stream
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Report LIB')
        # Define headers
        headers = ['NAME' ,'phone']
        for col, head in enumerate(headers):
            sheet.write(0, col, head)
        row = 1
        for part in partner_ids:
            sheet.write(row,0, part.name)
            sheet.write(row,1, part.phone)
            row+=1
        # Close the workbook
        workbook.close()
        output.seek(0)

        # Return the XLSX file as an HTTP response
        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename="sales_report.xlsx"')
            ]
        )
