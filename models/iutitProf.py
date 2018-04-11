# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_prof(models.Model):
    _name = 'iut.it.prof'
    _inherit = 'res.partner'

    name = fields.Char(string="Nom", required=True)