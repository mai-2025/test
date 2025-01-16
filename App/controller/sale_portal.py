import requests
from odoo import http
from odoo.http import request
import json
from odoo.http import Response

class Sale(http.Controller):
    #  auth_type= [public or user or none]
    @http.route('/my_sale_details', type="http", auth="public", website=True)
    def get_sale_orders(self, **kwargs):
        sale_details = request.env['sale.order'].sudo().search([])
        if not sale_details:
            print("No sale orders found.")
        else:
            print(sale_details)
        return request.render('App.sale_details_page', {'my_details': sale_details})


    @http.route('/new_request_submit', type="http", auth="user", website=True ,csrf=True)
    def request_submit(self, **kwargs):
        student_name = kwargs.get('st_name')
        company_name = kwargs.get('company_name')
        #if student_name:
             #Create a new record in the `student` model
        stu = request.env['student'].sudo().create({
                'st_name': student_name,
                'company_id': company_name,
                'active_name': True,
            })
        return "New Student record created successfully."


    @http.route('/student_get', type="http", auth="public", website=True ,csrf=False)
    def get_student_list(self, **kwargs):
        student_code = kwargs.get('code')

        # Search for student details based on the provided code (limit to 1 student)
        student_details = request.env['student'].sudo().search([('code', '=', student_code)], limit=1)
        print(student_details)
        if student_details:
                    print(student_details.st_name)
                    response_data = {
                        'student': {
                            'name': student_details.st_name,
                            'code': student_details.code
                        }
                    }
        return Response(json.dumps(response_data), content_type="application/json")
