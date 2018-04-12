# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_classe(models.Model):
    _name = 'iut.it.classe'

    name = fields.Char(string="Nom", required=True)
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Première'), ('terminale', 'Terminale')])
    nombre_eleve = fields.One2many(string="Nombre d'élèves", compute="_compute_o2m_field")

    @api.one
    def _compute_o2m_field(self):
        count = 0
        for each eleve in iut.it.eleve.object
            count ++
        self.nombre_eleve = count

