from django.test import TestCase
from cost_tracker.models import Cost
from cost_tracker.serializers import CostSerializer
from datetime import date


class CostSerializerTest(TestCase):
    def setUp(self):
        self.cost_data = {
            "category": "Utilities",
            "amount": 75.50,
            "date": date.today(),
        }
        self.serializer = CostSerializer(data=self.cost_data)

    def test_serializer_valid(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(
            self.serializer.validated_data["category"], self.cost_data["category"]
        )
        self.assertEqual(
            self.serializer.validated_data["amount"], self.cost_data["amount"]
        )
        self.assertEqual(self.serializer.validated_data["date"], self.cost_data["date"])
