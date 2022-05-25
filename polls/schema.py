import graphene
from graphene_django.types import DjangoObjectType

from .models import Question, Choice


class QuestionType(DjangoObjectType):

    class Meta:
        model = Question

class ChoiceType(DjangoObjectType):

    custom_param = graphene.String()

    class Meta:
        model = Choice

    def resolve_custom_param(self, info):
        return 42


class Query(object):
    question = graphene.Field(QuestionType, id=graphene.Int(), name=graphene.String())
    all_questions = graphene.List(QuestionType)

    my_name = graphene.Field(ChoiceType, st_id=graphene.String())
    all_choices = graphene.List(ChoiceType)
    
    this_is_query = graphene.Field(QuestionType)
    def resolve_this_is_query(self, info, **kwargs):
        return Question.objects.first()

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_all_choices(self, info, **kwargs):
        return Choice.objects.all()

    def resolve_my_name(self, info, **kwargs):
        st_id = kwargs.get('st_id')
        print(st_id)
        return Choice.objects.all().first()

    test = graphene.List(graphene.String, name=graphene.Int())

    def resolve_test(self, info, **kwargs):
        name = kwargs.get('name')
        return ["sangjin"]