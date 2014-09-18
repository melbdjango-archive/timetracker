from django.test import TestCase
from .models import Entry, Project, Client
from datetime import timedelta
from django.utils.timezone import now


class DurationTestCase(TestCase):
    def setUp(self):
        client = Client.objects.create(name="Darren's Sweet New Company")
        self.project = Project.objects.create(name="First Project", client=client)

    def test_duration_is_accurate(self):
        e = Entry.objects.create(
            title='Our first test time entry',
            project=self.project,
            start_time=now() - timedelta(minutes=55),
            end_time=now()
        )
        self.assertEqual(e.duration, 55)

        e2 = Entry.objects.create(
            title='Our first test time entry',
            project=self.project,
            start_time=now() - timedelta(minutes=550),
            end_time=now()
        )
        self.assertEqual(e2.duration, 550)

    def test_setting_duration_works(self):
        # create Entry with start time now - 30
        # end_time = now
        e = Entry.objects.create(
            title='Our first test time entry',
            project=self.project,
            start_time=now() - timedelta(minutes=30),
            end_time=now()
        )
        self.assertEqual(e.duration, 30)

        # set .duration = 5
        e.duration = 5

        # test .duration == starttime + timedelta(5)
        self.assertEqual(e.duration, 5)
        self.assertEqual(e.end_time, e.start_time + timedelta(minutes=5))
