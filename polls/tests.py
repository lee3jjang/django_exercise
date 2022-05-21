import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    
    def test_question_object_count(self):
        self.assertEqual(Question.objects.count(), 1)

    # def test_