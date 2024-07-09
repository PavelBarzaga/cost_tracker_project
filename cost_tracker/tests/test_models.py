from django.test import TestCase
from cost_tracker.models import Cost
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date


class CostModelTest(TestCase):
    def setUp(self):
        self.cost = Cost.objects.create(
            category="Groceries",
            amount=50.00,
            date=date.today(),
            file=SimpleUploadedFile("test_file.txt", b"file_content"),
        )

    def test_cost_creation(self):
        self.assertIsInstance(self.cost, Cost)
        self.assertEqual(self.cost.category, "Groceries")
        self.assertEqual(self.cost.amount, 50.00)
        self.assertEqual(self.cost.file.name, "cost_files/test_file.txt")
