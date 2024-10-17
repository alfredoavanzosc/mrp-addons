# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Mrp Product Loss Cost",
    "version": "16.0.1.0.0",
    "category": "Manufacturing/Manufacturing",
    "website": "https://github.com/avanzosc/mrp-addons",
    "author": "AvanzOSC",
    "license": "AGPL-3",
    "depends": [
        "mrp_stock_move_cost",
    ],
    "data": [
        "views/mrp_production_views.xml",
        "views/stock_scrap_views.xml",
    ],
    "installable": True,
}
