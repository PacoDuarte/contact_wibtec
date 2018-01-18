# -*- coding: utf-8 -*-
from odoo import http

# class ContactWibtec(http.Controller):
#     @http.route('/contact_wibtec/contact_wibtec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contact_wibtec/contact_wibtec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contact_wibtec.listing', {
#             'root': '/contact_wibtec/contact_wibtec',
#             'objects': http.request.env['contact_wibtec.contact_wibtec'].search([]),
#         })

#     @http.route('/contact_wibtec/contact_wibtec/objects/<model("contact_wibtec.contact_wibtec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contact_wibtec.object', {
#             'object': obj
#         })