import frappe
from frappe import _
from frappe.model.document import Document

@frappe.whitelist()
def create_task(**kwargs):
    try:
        task = frappe.new_doc("Task")
        task.update(kwargs)
        task.insert()
        return task.as_dict()
    except Exception as e:
        frappe.throw(_("Error creating task: {0}").format(str(e)))

@frappe.whitelist()
def get_task(name):
    try:
        task = frappe.get_doc("Task", name)
        return task.as_dict()
    except Exception as e:
        frappe.throw(_("Error fetching task: {0}").format(str(e)))

@frappe.whitelist()
def update_task(name, **kwargs):
    try:
        task = frappe.get_doc("Task", name)
        task.update(kwargs)
        task.save()
        return task.as_dict()
    except Exception as e:
        frappe.throw(_("Error updating task: {0}").format(str(e)))

@frappe.whitelist()
def delete_task(name):
    try:
        task = frappe.get_doc("Task", name)
        task.delete()  # Delete the task
        return {"message": f"Task '{name}' deleted successfully"}
    except Exception as e:
        frappe.throw(_("Error deleting task: {0}").format(str(e)))
