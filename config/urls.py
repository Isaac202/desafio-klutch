from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
