from odoo import models, fields, api
from odoo.exceptions import ValidationError


class paco_try(models.Model):
	_inherit = 'res.partner'
	
	@api.depends('country_id')
	def _calculate_region(self):
		for data in self:
			if data.country_id:
				if data.country_id.name == 'Germany':
					data.region = "ADD"
				elif data.country_id.name == 'Austria':
					data.region = "Oester"
				elif data.country_id.name == 'Switzerland':
					data.region = "CH"
				elif data.country_id.name == 'Leichtenstein':
					data.region = "CH"
				else:
					data.region = "AUSL"
					
	def _default_integer_copies(self):
		return 1

	first_name = fields.Char('First Name', size=16)
	last_name = fields.Char('Last Name', size=16)
	k_nr = fields.Integer('k-Nr')
	region = fields.Char(compute=_calculate_region ,string='Region')
	deliver_program_guide = fields.Boolean(string='Deliver program guide?', default=_default_integer_copies)
	n_copies = fields.Integer(string='No of copies', default=_default_integer_copies)
	reason = fields.Selection([('reason1','reason1'),('reason2','reason2')], string='Reason for cancelling')
	no_thankyou_letter = fields.Boolean('No thank you letters?')
	date_ = fields.Date('Date created')

	_sql_constraints = [
		('k_nr', 'unique(k_nr)', 'Please enter Unique k-Nr'),
	]
