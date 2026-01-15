from odoo import models, fields

class OrderSale(models.Model):
    _inherit = "sale.order"

    code_reference = fields.Char(
        string="Code Reference"
    )
