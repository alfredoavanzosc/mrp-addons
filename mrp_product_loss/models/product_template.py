# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_loss_qty = fields.Float(
        string="Loss in products to be consumed",
        digits="Product Unit of Measure",
        default="0.0",
    )
