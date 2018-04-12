# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class iut_it_eleve(models.Model):
    _name = 'iut.it.eleve'

    name = fields.Char(string="Nom", required=True)
    surname = fields.Char(string="Prénom")
    birthday = fields.Date(date="Date de naissance")
    age = fields.Integer(compute='age_method')
    nom_classe = fields.Char(string="Nom de la classe", required=True)

    @api.onchange('birthday')
    def age_method(self):
        self.age = (datetime.datetime.today()) - self.birthday