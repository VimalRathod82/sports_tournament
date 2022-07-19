from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Sports Master"),
			"icon": "fa fa-group",
			"items": [
				{
					"type": "doctype",
					"name": "Tournament",
					"description": _("Tournament")
				},
				{
					"type": "doctype",
					"name": "Game",
					"description": _("Game")
				},
				{
					"type": "doctype",
					"name": "Sports Ground",
					"description": _("Sports Ground")
				},
				{
					"type": "doctype",
					"name": "Player Type",
					"description": _("Player Type")
				},
				{
					"type": "doctype",
					"name": "Player",
					"description": _("Player")
				},
				{
					"type": "doctype",
					"name": "Sport Group",
					"description": _("Sport Group")
				},
				{
					"type": "doctype",
					"name": "Award Category",
					"description": _("Award Category")
				}
			]
		},
		{
			"label": _("Sports Details"),
			"icon": "fa fa-lock",
			"items": [
				{
					"type": "doctype",
					"name": "Sport Team",
					"description": _("Sport Team")
				},
				{
					"type": "doctype",
					"name": "Match",
					"description": _("Match")
				}
			]
		},
		{
			"label": _("Sports Reports"),
			"icon": "fa fa-lock",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Award Category Report",
					"doctype": "Match"
				}
			]
		}
	]