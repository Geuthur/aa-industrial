"""Industry for a TestView class."""

from http import HTTPStatus

from django.test import RequestFactory, TestCase
from django.urls import reverse

from app_utils.testdata_factories import UserMainFactory

from industry.views import index


class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.factory = RequestFactory()
        cls.user = UserMainFactory(
            permissions=[
                "industry.basic_access",
            ]
        )

    def test_view(self):
        request = self.factory.get(reverse("industry:index"))
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
