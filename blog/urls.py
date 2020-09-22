from django.urls import path 
from .views import BlogListView , BlogDetailView ,BlogCreateView , BlogUpdateView ,BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name = 'posts'),
    path( 'post/<int:pk>/',BlogDetailView.as_view(), name = 'post_details' ),
    path('post/new/',BlogCreateView.as_view(), name = 'new_post' ) ,
    path('post/<int:pk>/edet', BlogUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delet' , BlogDeleteView.as_view(), name ='post_delet' )

]

