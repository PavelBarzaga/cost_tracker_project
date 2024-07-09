from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cost_tracker.models import Cost
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile


class CostAPITest(APITestCase):
    def setUp(self):
        self.cost = Cost.objects.create(
            category="Entertainment",
            amount=100.00,
            date=date.today(),
            file=SimpleUploadedFile("test_file.txt", b"file_content"),
        )
        self.valid_payload = {
            "category": "Transport",
            "amount": 20.00,
            "date": date.today(),
        }
        self.invalid_payload = {"category": "", "amount": 20.00, "date": date.today()}

    def test_get_costs(self):
        response = self.client.get(reverse("cost-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_valid_cost(self):
        response = self.client.post(
            reverse("cost-list-create"), self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_cost(self):
        response = self.client.post(
            reverse("cost-list-create"), self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_cost(self):
        response = self.client.get(
            reverse("cost-retrieve-update-destroy", kwargs={"pk": self.cost.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_cost(self):
        new_data = {
            "category": "Updated Category",
            "amount": 150.00,
            "date": date.today(),
        }
        response = self.client.put(
            reverse("cost-retrieve-update-destroy", kwargs={"pk": self.cost.pk}),
            new_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cost.refresh_from_db()
        self.assertEqual(self.cost.category, new_data["category"])
        self.assertEqual(self.cost.amount, new_data["amount"])

    def test_delete_cost(self):
        response = self.client.delete(
            reverse("cost-retrieve-update-destroy", kwargs={"pk": self.cost.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
