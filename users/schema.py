import graphene
from graphene_django import DjangoObjectType

from users.models import UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return UserModel.objects.all()


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, name, last_name):
        return CreateUser(
            user=UserModel.objects.create(name=name, last_name=last_name)
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
