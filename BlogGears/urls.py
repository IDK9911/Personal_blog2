from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='landing_page'),
    path("posts",views.showAll,name='posts_page'),
    path('posts/<slug:slug>',views.postDetail,name='post_detail_page')
]
