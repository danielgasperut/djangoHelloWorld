"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PollMethodTests(TestCase):
  def test_was_published_recently_with_future_poll(self):
    #should return false
    future_poll = Poll(pub_date = timezone.now() + datetime.timedelta(days=30))
    self.assertEqual(future_poll.was_published_recently(),False)

  def test_was_published_recently_with_old_poll(self):
    #should return false
    future_poll = Poll(pub_date = timezone.now() - datetime.timedelta(days=30))
    self.assertEqual(future_poll.was_published_recently(),False)
    
  def test_was_published_recently_with_recent_poll(self):
    #should return false
    future_poll = Poll(pub_date = timezone.now() - datetime.timedelta(hours=1))
    self.assertEqual(future_poll.was_published_recently(),True) 
