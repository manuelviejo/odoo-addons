# -*- coding: utf-8 -*-
# Copyright (c) 2018 Alexander Ezquevo <alexander@acysos.com>
# Copyright (c) 2018 Ignacio Ibeas Izquierdo <ignacio@acysos.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    payroll_extid = fields.Char(string='Payroll reference')
    payroll_account = fields.Many2one(
        string='Payroll account', comodel_name='account.account')
