app_name = "pixfar_shipment"
app_title = "Pixfar Shipment"
app_publisher = "Pixfar"
app_description = "A shipment managemet apps for overide default features"
app_email = "query@pixfar.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pixfar_shipment/css/pixfar_shipment.css"
# app_include_js = "/assets/pixfar_shipment/js/pixfar_shipment.js"

# include js, css files in header of web template
# web_include_css = "/assets/pixfar_shipment/css/pixfar_shipment.css"
# web_include_js = "/assets/pixfar_shipment/js/pixfar_shipment.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pixfar_shipment/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Fixtures

fixtures = ["Custom Field"]


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "pixfar_shipment.utils.jinja_methods",
# 	"filters": "pixfar_shipment.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pixfar_shipment.install.before_install"
# after_install = "pixfar_shipment.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pixfar_shipment.uninstall.before_uninstall"
# after_uninstall = "pixfar_shipment.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pixfar_shipment.utils.before_app_install"
# after_app_install = "pixfar_shipment.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pixfar_shipment.utils.before_app_uninstall"
# after_app_uninstall = "pixfar_shipment.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pixfar_shipment.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Task": "pixfar_shipment.overrides.SendMailToCustomer"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pixfar_shipment.tasks.all"
# 	],
# 	"daily": [
# 		"pixfar_shipment.tasks.daily"
# 	],
# 	"hourly": [
# 		"pixfar_shipment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pixfar_shipment.tasks.weekly"
# 	],
# 	"monthly": [
# 		"pixfar_shipment.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "pixfar_shipment.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pixfar_shipment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pixfar_shipment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pixfar_shipment.utils.before_request"]
# after_request = ["pixfar_shipment.utils.after_request"]

# Job Events
# ----------
# before_job = ["pixfar_shipment.utils.before_job"]
# after_job = ["pixfar_shipment.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"pixfar_shipment.auth.validate"
# ]
