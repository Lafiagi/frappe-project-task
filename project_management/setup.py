import frappe

def after_install():
    # Create Task DocType
    if not frappe.db.exists("DocType", "Task"):
        task = frappe.new_doc("DocType")
        task.name = "Task"
        task.module = "Project Management"

        # Create fields properly
        task.append("fields", {
            "fieldname": "title",
            "label": "Title",
            "fieldtype": "Data",
            "reqd": 1
        })

        task.append("fields", {
            "fieldname": "description",
            "label": "Description",
            "fieldtype": "Text Editor"
        })

        task.append("fields", {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "\nOpen\nIn Progress\nCompleted",
            "default": "Open"
        })

        task.append("fields", {
            "fieldname": "due_date",
            "label": "Due Date",
            "fieldtype": "Date"
        })

        task.append("fields", {
            "fieldname": "assigned_to",
            "label": "Assigned To",
            "fieldtype": "Link",
            "options": "User"
        })

        task.insert()

    # Create Project DocType
    if not frappe.db.exists("DocType", "Project"):
        project = frappe.new_doc("DocType")
        project.name = "Project"
        project.module = "Project Management"

        project.append("fields", {
            "fieldname": "project_name",
            "label": "Project Name",
            "fieldtype": "Data",
            "reqd": 1
        })

        project.append("fields", {
            "fieldname": "description",
            "label": "Description",
            "fieldtype": "Text Editor"
        })

        project.append("fields", {
            "fieldname": "start_date",
            "label": "Start Date",
            "fieldtype": "Date",
            "reqd": 1
        })

        project.append("fields", {
            "fieldname": "end_date",
            "label": "End Date",
            "fieldtype": "Date"
        })

        project.append("fields", {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": "\nPlanning\nActive\nCompleted\nOn Hold",
            "default": "Planning"
        })

        project.insert()

    # Create Project Task DocType
    if not frappe.db.exists("DocType", "Project Task"):
        project_task = frappe.new_doc("DocType")
        project_task.name = "Project Task"
        project_task.module = "Project Management"

        project_task.append("fields", {
            "fieldname": "project",
            "label": "Project",
            "fieldtype": "Link",
            "options": "Project",
            "reqd": 1
        })

        project_task.append("fields", {
            "fieldname": "task",
            "label": "Task",
            "fieldtype": "Link",
            "options": "Task",
            "reqd": 1
        })

        project_task.insert()
