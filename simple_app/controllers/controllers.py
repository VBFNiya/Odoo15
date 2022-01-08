# -*- coding: utf-8 -*-
# from odoo import http


# class SimpleApp(http.Controller):
#     @http.route('/simple_app/simple_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simple_app/simple_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('simple_app.listing', {
#             'root': '/simple_app/simple_app',
#             'objects': http.request.env['simple_app.simple_app'].search([]),
#         })

#     @http.route('/simple_app/simple_app/objects/<model("simple_app.simple_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simple_app.object', {
#             'object': obj
#         })
