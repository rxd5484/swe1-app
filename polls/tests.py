from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question


class PollsSmokeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = Question.objects.create(
            question_text="Favorite color?", pub_date=timezone.now()
        )
        cls.choice = Choice.objects.create(question=cls.question, choice_text="Blue")

    def test_poll_index_loads(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Favorite color?")

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Favorite color?")

    def test_vote_updates_choice_count(self):
        url = reverse("polls:vote", args=[self.question.pk])
        response = self.client.post(url, {"choice": self.choice.pk})
        self.assertRedirects(
            response, reverse("polls:results", args=[self.question.pk])
        )
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)

    def test_health_check_accepts_private_ip_host(self):
        response = self.client.get("/health/", HTTP_HOST="10.0.0.10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")
