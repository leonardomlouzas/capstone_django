from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser
from django.test import TestCase

from accounts.models import Account


class AccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = 'littletonclaire@lost.com'
        cls.password = 'wW*8uuuu'
        cls.user_obj: Account = Account.objects.create_user(
            email=cls.email, password=cls.password
        )

    def test_user_fields(self):
        self.assertIsInstance(self.user_obj.email, str)
        self.assertEqual(self.user_obj.email, self.email)

        self.assertIsInstance(self.user_obj.password, str)
        self.assertTrue(check_password(self.password, self.user_obj.password))

        self.assertIsInstance(self.user_obj, AbstractUser)
