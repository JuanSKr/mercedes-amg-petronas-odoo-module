from odoo import models, fields, api

class Motores(models.Model):
    _name = 'motores'

    name = fields.Char(string="Nombre del motor", required=True)
    potencia = fields.Integer(string="Potencia del motor (HP)")
    rpm_max = fields.Integer(string="RPM Máximas")
    torque_max = fields.Float(string="Torque Máximo (Nm)")
    fabrica_id = fields.Many2one(comodel_name="fabrica", string="Fabrica", required=True)
    image = fields.Binary(string="Image")
    eficiencia = fields.Float(string="Eficiencia del motor", compute="_calcular_eficiencia")

    @api.depends('potencia', 'rpm_max')
    def _calcular_eficiencia(self):
        for record in self:
            if record.rpm_max:
                record.eficiencia = record.potencia / record.rpm_max * 100
            else:
                record.eficiencia = 0