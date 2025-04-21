from odoo import fields, models

SALE_ORDER_PRODUCTION_STATE = [
    ("without", "Sin Producción"),
    ("production", "En Producción"),
    ("production_done", "Producción Terminada"),
]


class SaleOrder(models.Model):
    _inherit = "sale.order"

    production_state = fields.Selection(
        selection=SALE_ORDER_PRODUCTION_STATE,
        string="Producción",
        readonly=True,
        copy=False,
        index=True,
        tracking=3,
        default="without",
    )
    production_note = fields.Html("Notas de Producción")

    def action_production(self):
        self.ensure_one()
        self.production_state = "production"
        self.message_post(body="La orden de venta ha pasado a producción.")

    def action_production_done(self):
        self.ensure_one()
        self.production_state = "production_done"
        self.message_post(body="Producción terminada. Ahora se puede facturar.")
