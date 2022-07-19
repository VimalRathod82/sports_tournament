from __future__ import unicode_literals
import frappe
from frappe import _

def get_data():
	return [
		{
			"module_name": "Sports Tournament",
			"category": "Modules",
			"label": _("Sports Tournament"),
			"color": "#FFF5A7",
			#"reverse": 1,
			"icon": "octicon octicon-calendar",
			"type": "module",
			"description": "Todos, notes, calendar and newsletter."
		},
	]
