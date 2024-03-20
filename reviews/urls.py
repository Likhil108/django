from . import views
from django.urls import path
from .views import*

from django.contrib import admin
from django.urls import path
from .views import *


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', review_list, name='review_list'),
    path('add_review/', add_review, name='add_review')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
