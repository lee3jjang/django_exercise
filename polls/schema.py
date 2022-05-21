import graphene
from graphene_django.types import DjangoObjectType

from .models import Question, Choice


class QuestionType(DjangoObjectType):

    class Meta:
        model = Question

class ChoiceType(DjangoObjectType):

    class Meta:
        model = Choice


class Query(object):
    question = graphene.Field(QuestionType, id=graphene.Int(), name=graphene.String())
    all_questions = graphene.List(QuestionType)

    choice = graphene.Field(ChoiceType, id=graphene.Int(), name=graphene.String())
    all_choices = graphene.List(ChoiceType)

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_all_choices(self, info, **kwargs):
        return Choice.objects.all()
