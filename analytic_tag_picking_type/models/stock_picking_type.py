# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PickingType(models.Model):
    _inherit = 'stock.picking.type'

    analytic_tag_id = fields.Many2one(
        'account.analytic.tag', string='Analytic Tag', company_dependent=True)

