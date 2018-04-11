# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_agenda(models.Model):
    _name = 'iut.it.agenda'

    room = fields.Char(string="Salle")
    start = fields.datetime(string='Horaire de début')
    end = fields.datetime(string='Horaire de fin')
