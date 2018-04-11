# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_cours(models.Model):
    _name = 'iut.it.cours'

    name = fields.Char(string="Marque", required=True)
