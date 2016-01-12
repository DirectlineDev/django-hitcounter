from datetime import datetime, timedelta
from django.test import TestCase
from .models import Counter, DummyModel


class CounterTestCase(TestCase):
    def setUp(self):
        DummyModel.objects.create(dummy_field=1)

    def test_hit(self):
        dummy = DummyModel.objects.get(dummy_field=1)
        Counter.hit(dummy)
        Counter.hit(dummy, 2)
        self.assertEqual(3, Counter.objects.for_model(dummy, total=True))

        Counter.hit(dummy, date=datetime.today().date() - timedelta(days=1))
        Counter.hit(dummy, amount=3, date=datetime.today().date() - timedelta(days=1))
        self.assertEqual(7, Counter.objects.for_model(dummy, total=True))
        self.assertEqual(2, Counter.objects.for_model(dummy).count())

