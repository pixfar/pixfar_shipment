import frappe
from erpnext.projects.doctype.task.task import Task


class SendMailToCustomer(Task):
    def on_update(self):
        old_doc = self.get_doc_before_save()
        if old_doc and old_doc.status != self.status:
            print("\n\n ", self.exp_start_date,"\n\n ")
            # Fetch recipients from the Shipment Customer linked to the project
            recipients = frappe.db.sql(f"""
                SELECT email_id 
                FROM `tabShipment Customer` 
                WHERE `parent` = %s
            """, (self.name,), as_dict=True)

            recipient_emails = [recipient['email_id'] for recipient in recipients if recipient['email_id']]
            if recipient_emails:
                # Enqueue email sending
                frappe.enqueue(
                    'frappe.sendmail',
                    recipients=recipient_emails,
                    subject="Shipment Notification",
                    template='shipment_mail_template',
                    args=dict(
                        shipment_name=self.project,
                        start_date=self.exp_start_date,
                        status=self.status
                    ),
                    delayed=False
                )
                frappe.msgprint(f"Notification sent to: {', '.join(recipient_emails)}")
