# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    scrap_cost = fields.Float(digits="Product Price", copy=False)
    total_cost = fields.Float(
        string="Total MO Cost", digits="Product Price", copy=False
    )

    def update_prodution_cost(self):
        result = super().update_prodution_cost()
        scrap_cost = 0
        price_unit_cost = 0
        if self.scrap_ids:
            scrap_cost = sum(self.scrap_ids.mapped("scrap_cost"))
        total_of_cost = self.cost + scrap_cost
        if total_of_cost and self.move_finished_ids:
            for move in self.move_finished_ids:
                if move.quantity_done > 0:
                    move.price_unit_cost = total_of_cost / move.quantity_done
        if total_of_cost and self.qty_producing:
            price_unit_cost = total_of_cost / self.qty_producing
        self.scrap_cost = scrap_cost
        self.total_cost = total_of_cost
        self.price_unit_cost = price_unit_cost
        if self.lot_producing_id:
            self.lot_producing_id.with_context(from_production=True).purchase_price = (
                price_unit_cost
            )
        return result
