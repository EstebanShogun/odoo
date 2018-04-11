# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_type(models.Model):
    _name = 'iut.it.type'

    name = fields.Char(string="Type")
    