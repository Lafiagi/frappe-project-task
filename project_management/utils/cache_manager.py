import frappe
from frappe.utils.caching import redis_cache

@redis_cache(ttl=300)  # Cache for 5 minutes
def get_cached_task(name):
    return frappe.get_doc("Task", name)

# Optimized API endpoint
@frappe.whitelist()
def get_project_tasks(project_name):
    # Use index on project field, to optimize search
    tasks = frappe.get_all(
        "Project Task",
        filters={"project": project_name},
        fields=["task"],
        order_by="creation desc",
        limit_page_length=20  # pagination
    )

    # Batch fetch tasks
    task_names = [t.task for t in tasks]
    tasks_data = frappe.get_all(
        "Task",
        filters={"name": ["in", task_names]},
        fields=["*"]
    )

    return tasks_data
