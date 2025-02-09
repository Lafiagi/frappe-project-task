import unittest
import frappe
from frappe.tests.utils import FrappeTestCase
from project_management.api.api import create_task, get_task, update_task, delete_task


class TestTaskAPI(FrappeTestCase):
    def test_task_crud(self):
        # Test Create
        task_data = {
            "title": "API Test Task",
            "description": "Testing API endpoints",
            "status": "Open",
        }
        task = create_task(**task_data)
        self.assertEqual(task.title, task_data["title"])

        # Test Read
        fetched_task = get_task(task.name)
        self.assertEqual(fetched_task.title, task_data["title"])

        # Test Update
        updated_data = {"status": "In Progress"}
        updated_task = update_task(task.name, **updated_data)
        self.assertEqual(updated_task.status, "In Progress")

        # Test Delete
        delete_task(task.name)
        self.assertFalse(frappe.db.exists("Task", task.name))
