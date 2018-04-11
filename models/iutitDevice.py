# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_device(models.Model):
    _name = 'iut.it.device'

    name = fields.Char(string="Appareil")
    date_allocation = fields.Date(string="Date d'acquisition")
    serial_number = fields.Char(string="Numéro de série")
    date_purchase = fields.Date(string="Date d'achat")
    date_warranty_end = fields.Date(string="Date de fin de garantie")
