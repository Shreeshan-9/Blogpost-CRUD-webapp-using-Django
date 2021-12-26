from django.urls import path
from . views import (PostListView, PostDetailView, 
                        PostCreateView, PostUpdateView
                        , PostDeleteView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),

    # for the detail view of a post where the post_id can be a part of the route:
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),


    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('about/', views.about, name='blog-about'),
]


# for the DetailView url, we need to create a URL pattern that contains a variable
# path('post/<data_type:variable_name>/')
