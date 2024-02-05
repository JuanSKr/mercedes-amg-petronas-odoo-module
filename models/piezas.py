from odoo import models, fields, api

class Piezas(models.Model):
    _name = 'piezas'

    name = fields.Char(string="Nombre de la pieza", required=True)
    cantidad = fields.Integer(string="Cantidad de piezas", required=True)
    precio = fields.Float(string="Precio de la pieza", required=True)
    descripcion = fields.Text(string="Descripción de la pieza", required=True)
    decimas_ganancia = fields.Integer(string="Decimas de ganancia", required=True)
    fecha_fabricacion= fields.Date(string="Fecha de fabricación", required=True)
    fabrica = fields.Many2one(comodel_name="fabrica", string="Fabrica", required=True)
    piloto_id = fields.Many2one(comodel_name="piloto", string="Piloto", required=True)
    image = fields.Binary(string="Image")
    tipo_pieza = fields.Selection([
        ('motor', 'Motor'),
        ('chasis', 'Chasis'),
        ('frenos', 'Frenos'),
        ('llantas', 'Llantas'),
        ('suspension', 'Suspensión'),
        ('transmision', 'Transmisión')
    ], string="Tipo de Pieza", required=True)
    precio_total = fields.Float(string="Precio Total", compute='_compute_precio_total')

    @api.depends('precio', 'cantidad')
    def _compute_precio_total(self):
        for record in self:
            record.precio_total = record.precio * record.cantidad