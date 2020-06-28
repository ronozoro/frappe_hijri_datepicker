# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_hijri_datepicker"
app_title = "Hijri Datepicker"
app_publisher = "Mostafa Mohamed"
app_description = "The Hijri(Islamic) calendar is the official calendar in countries around the Gulf, especially Saudi Arabia."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "m.dev.odoo@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_hijri_datepicker/css/frappe_hijri_datepicker.css"
# app_include_js = "/assets/frappe_hijri_datepicker/js/frappe_hijri_datepicker.js"
app_include_css = [
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/redmond.calendars.picker.css",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.timeentry.package-2.0.1/jquery.timeentry.css",
    "/assets/frappe_hijri_datepicker/css/frappe_hijri_datepicker.css"]
app_include_js = [
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.plugin.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.all.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.plus.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.picker.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.islamic.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.islamic-ar.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.calendars.package-2.0.2/jquery.calendars.islamic-fa.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.timeentry.package-2.0.1/jquery.plugin.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.timeentry.package-2.0.1/jquery.timeentry.js",
    "/assets/frappe_hijri_datepicker/js/lib/jquery.timeentry.package-2.0.1/jquery.timeentry-ar.js",
    "/assets/frappe_hijri_datepicker/js/frappe_hijri_datepicker.js",
]
# include js, css files in header of web template
# web_include_css = "/assets/frappe_theme/css/lightbox.css"
# web_include_js = ["/assets/frappe_theme/js/lightbox.min.js",
# 	"/assets/manual_erpnext_com/js/setup_lightbox.js"]

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
# get_website_user_home_page = "frappe_hijri_datepicker.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_hijri_datepicker.install.before_install"
# after_install = "frappe_hijri_datepicker.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_hijri_datepicker.notifications.get_notification_config"

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
# 		"frappe_hijri_datepicker.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_hijri_datepicker.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_hijri_datepicker.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_hijri_datepicker.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_hijri_datepicker.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_hijri_datepicker.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_hijri_datepicker.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_hijri_datepicker.task.get_dashboard_data"
# }
