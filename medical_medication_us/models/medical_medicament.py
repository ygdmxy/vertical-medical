# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models


class MedicalMedicament(models.Model):
    _inherit = 'medical.medicament'
    ndc = fields.Char(
        string='NDC',
        help='National Drug Code for medication'
    )
    control_code = fields.Selection([
        ('c1', 'C1'),
        ('c2', 'C2'),
        ('c3', 'C3'),
        ('c4', 'C4'),
        ('c5', 'C5'),
    ],
        help='Federal drug scheduling code',
    )
