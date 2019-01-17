# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_id')
    def onchange_product_id(self):
        res = super(PurchaseOrderLine, self).onchange_product_id()
        if self.product_id:
            if self.order_id.picking_type_id.analytic_tag_id:
                self.analytic_tag_ids = [(4, self.order_id.picking_type_id.analytic_tag_id.id)]

        return res

    @api.model
    def create(self, vals):
        if vals.get('product_id') and not vals.get('analytic_tag_id'):
            if self.order_id.picking_type_id.analytic_tag_id:
                vals['analytic_tag_ids'] = [(6, self.order_id.picking_type_id.analytic_tag_id.id)]
        return super(PurchaseOrderLine, self).create(vals)

