# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sports_tournament"
app_title = "Sports Tournament"
app_publisher = "VVSD"
app_description = "Sports Tournament Managemnet System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vimalrathod@vvsdtz.com"
app_license = "GPL"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sports_tournament/css/sports_tournament.css"
# app_include_js = "/assets/sports_tournament/js/sports_tournament.js"

# include js, css files in header of web template
# web_include_css = "/assets/sports_tournament/css/sports_tournament.css"
# web_include_js = "/assets/sports_tournament/js/sports_tournament.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sports_tournament.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sports_tournament.install.before_install"
# after_install = "sports_tournament.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sports_tournament.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sports_tournament.tasks.all"
# 	],
# 	"daily": [
# 		"sports_tournament.tasks.daily"
# 	],
# 	"hourly": [
# 		"sports_tournament.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sports_tournament.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sports_tournament.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sports_tournament.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sports_tournament.event.get_events"
# }

