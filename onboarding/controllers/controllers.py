# -*- coding: utf-8 -*-
# from odoo import http


# class Onboarding(http.Controller):
#     @http.route('/onboarding/onboarding/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/onboarding/onboarding/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('onboarding.listing', {
#             'root': '/onboarding/onboarding',
#             'objects': http.request.env['onboarding.onboarding'].search([]),
#         })

#     @http.route('/onboarding/onboarding/objects/<model("onboarding.onboarding"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('onboarding.object', {
#             'object': obj
#         })
