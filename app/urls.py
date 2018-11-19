from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

graphql_view = GraphQLView.as_view(graphiql=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', graphql_view),
]
