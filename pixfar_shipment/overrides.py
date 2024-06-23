import frappe
from erpnext.projects.doctype.task.task import Task


class SendMailToCustomer(Task):
    def on_update(self):
        old_doc = self.get_doc_before_save()
        if old_doc and old_doc.status != self.status:
            frappe.enqueue(frappe.sendmail(
                recipients=self.custom_customer_email,
                subject="Shipment Notificaiton",
                template='shipment_mail_template',
                args=dict(
                customer_name=self.custom_customer,
                shipment_name=self.project,
                start_date=self.exp_start_date,
                start_time=self.expected_time,
                status=self.status
                ),
                delayed=False
            ))
            
