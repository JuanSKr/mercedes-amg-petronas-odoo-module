from odoo import models, fields

class Fabrica(models.Model):
    _name = 'fabrica'

    name = fields.Char(string="Nombre de la fábrica", required=True)
    ubicacion = fields.Char(string="Ubicación de la fábrica")
    contacto = fields.Char(string="Contacto de la fábrica")
    image = fields.Binary(string="Image")