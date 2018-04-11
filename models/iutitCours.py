# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_agenda(models.Model):
    _name = 'iut.it.agenda'

    name = fields.Char(string="Marque", required=True)
    warranty_delay_month = fields.Integer(string="Mois sous garantie")
    support_phone = fields.Char(string="Numéro de téléphone")
