from django.conf.urls import url
from store.views import Index

urlpatterns = [
    url(r'^$', Index.as_view()),
]
