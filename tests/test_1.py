from flask import url_for

from app import app
from .models import Bulletins


class UserViewsTests(BaseTestCase):
    def test_users_can_login(self):
        User.create(name='Joe', email='joe@joes.com', password='12345')

        response = self.client.post(url_for('users.login'),
                                    data={'email': 'joe@joes.com', 'password': '12345'})

        self.assert_redirects(response, url_for('tracking.index'))
