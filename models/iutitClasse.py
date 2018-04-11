# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_classe(models.Model):
    _name = 'iut.it.classe'

    name = fields.Char(string="Nom", required=True)
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Première'), ('terminale', 'Terminale')])

