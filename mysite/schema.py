import graphene

from polls.schema import Query as PollsQuery

class Query(PollsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)