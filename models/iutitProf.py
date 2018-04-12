# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_it_prof(models.Model):
    _name = 'iut.it.prof'
    _inherit = 'res.partner'

    name = fields.Char(string="Nom", required=True)
    classe = fields.Char(string="Classe")
    presence = fields.One2many(string="Doit être présent",compute="_compute_o2m_field")

    @api.one
    def _compute_o2m_field(self):
        related_recordset = self.env["Agenda.obj"].search([([Agenda.start, Agenda.start] , Agenda.classe == self.classe)])
        self.presence = related_recordset