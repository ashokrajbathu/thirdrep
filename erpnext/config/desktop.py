from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Accounts": {
			"color": "#3498db",
			"icon": "octicon octicon-repo",
			"label": _("Finance"),
			"type": "module"
		},
		"Buying": {
			"color": "#c0392b",
			"label": _("Loans"),
			"icon": "icon-shopping-cart",
			"icon": "octicon octicon-briefcase",
			"type": "module"
		},
		"HR": {
			"color": "#2ecc71",
			"icon": "icon-group",
			"icon": "octicon octicon-organization",
			"label": _("Human Resources"),
			"type": "module"
		},
#		"Manufacturing": {
#			"color": "#7f8c8d",
#			"icon": "icon-cogs",
#			"icon": "octicon octicon-tools",
#			"type": "module"
#		},
		"POS": {
			"color": "#589494",
			"icon": "icon-th",
			"icon": "octicon octicon-credit-card",
			"type": "page",
			"link": "pos"
		},
		"Projects": {
			"color": "#8e44ad",
			"icon": "icon-puzzle-piece",
			"icon": "octicon octicon-rocket",
			"type": "module"
		},
		"Selling": {
			"color": "#1abc9c",
			 "label": _("Deposits"),
			"icon": "icon-tag",
			"icon": "octicon octicon-tag",
			"type": "module"
		},
#		"CRM": {
#			"color": "#EF4DB6",
#			"label": _("Customers"),
#			"icon": "octicon octicon-broadcast",
#			"type": "module"
#		},
		"Stock": {
			"color": "#f39c12",
			"icon": "icon-truck",
			"label": _("Products"),
			"icon": "octicon octicon-package",
			"type": "module"
		},
		"Support": {
			"color": "#2c3e50",
			"icon": "icon-phone",
			"icon": "octicon octicon-issue-opened",
			"type": "module"
		},
#		"Learn": {
#			"color": "#FCB868",
#			"force_show": True,
#			"icon": "icon-facetime-video",
#			"type": "module",
#			"is_help": True
#		}
	}
