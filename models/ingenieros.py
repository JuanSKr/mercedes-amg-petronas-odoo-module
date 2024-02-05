from odoo import models, fields

class Ingeniero(models.Model):
    _name = 'ingenieros'

    name = fields.Char(string="Nombre del Ingeniero", required=True)
    experiencia = fields.Integer(string="Años de Experiencia", required=True)
    especialidad = fields.Selection([
        ('motor', 'Ingeniero de Motores'),
        ('chasis', 'Ingeniero de Chasis'),
        ('estratega', 'Ing. Estratega de Carrera'),
        ('pista', 'Ingeniero de Pista'),
        ('aerodinamico', 'Ingeniero Aerodinámico'),
        ('telemetria', 'Ingeniero de Telemetría'),

    ], string="Especialidad", required=True)
    fecha_contratacion = fields.Date(string="Fecha de Contratación", required=True)
    salario = fields.Float(string="Salario", required=True)
    piloto_id = fields.Many2one(comodel_name="piloto", string="Piloto")
    fabrica = fields.Many2one(comodel_name="fabrica", string="Fabrica", required=True)
    image = fields.Binary(string="Imagen")