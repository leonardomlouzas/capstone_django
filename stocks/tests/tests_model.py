from django.test import TestCase
from stocks.models import Stock

class StockModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        cls.quantity = 5

        cls.stock = Stock.objects.create(quantity=cls.quantity)

    def test_stock_field(self) -> None:
        self.assertIsInstance(self.stock, int)
        self.assertEqual(self.stock.quantity, self.quantity )
