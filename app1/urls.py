from django.urls import path
from .views import (ListContentView,DetailContentView,
                    UpdateContentView,DeleteContentView,CreateContentView)

urlpatterns = [
    path('all_content',ListContentView.as_view()),
    path('detail/<int:content_id>',DetailContentView.as_view()),
    path('update/<int:content_id>',UpdateContentView.as_view()),
    path('create/',CreateContentView.as_view()),
    path('delete/<int:content_id>',DeleteContentView.as_view())

]