from django.conf.urls import url


from .views import blog_index

urlpatterns = [
    url(r'', blog_index),
]

