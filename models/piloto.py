from odoo import models, fields

class Piloto(models.Model):
    _name= 'piloto'

    name = fields.Char(string='Piloto', required=True)
    image = fields.Binary(string="Image")