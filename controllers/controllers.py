# -*- coding: utf-8 -*-
from odoo import http

# class Vetapp(http.Controller):
#     @http.route('/vetapp/vetapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vetapp/vetapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vetapp.listing', {
#             'root': '/vetapp/vetapp',
#             'objects': http.request.env['vetapp.vetapp'].search([]),
#         })

#     @http.route('/vetapp/vetapp/objects/<model("vetapp.vetapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vetapp.object', {
#             'object': obj
#         })