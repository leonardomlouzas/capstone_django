from faker import Faker
from rest_framework.test import APITestCase

from accounts.models import Account


class AccountViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker()
        cls.url = '/api/accounts/'
        cls.user_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
        }
        cls.invalid_user_data = {
            'email': fake.email(),
        }

    def test_create_user(self) -> None:
        response = self.client.post(self.url, self.user_data)

        self.assertEqual(response.status_code, 201)
        self.assertNotIn('password', response.json())

    def test_create_user_fails(self) -> None:
        response = self.client.post(self.url, self.invalid_user_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.json())


class LoginViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        fake = Faker()
        cls.url = '/api/login/'
        cls.user_data = {'email': fake.email(), 'password': fake.password()}
        cls.user_data_wrong_pass = {
            'email': fake.email(),
            'password': fake.password(),
        }
        cls.user_data_wrong_body = {'email': fake.email()}

    def setUp(self) -> None:
        Account.objects.create_user(**self.user_data)

    def test_login(self) -> None:
        response = self.client.post(self.url, self.user_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json())

    def test_login_fail_invalid_credentials(self) -> None:
        response = self.client.post(self.url, self.user_data_wrong_pass)

        self.assertEqual(response.status_code, 401)
        self.assertDictEqual(
            response.json(), {'detail': 'invalid email or password'}
        )

    def test_login_fail_invalid_body(self) -> None:
        response = self.client.post(self.url, self.user_data_wrong_body)

        self.assertEqual(response.status_code, 400)
        self.assertIn('password', response.json())
        self.assertDictEqual(
            response.json(), {'password': ['This field is required.']}
        )
