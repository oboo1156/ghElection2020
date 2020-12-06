from django.urls import path
from .views import RegionDetailView,RegionListView,HomeView,CommentFormView


app_name = 'abatoo'
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('regions/',RegionListView.as_view(),name='list'),
    path('regions/<int:pk>/',RegionDetailView.as_view(),name='detail'),
    path('regions/<int:pk>/comment',CommentFormView.as_view(),name='comment_add'),
]