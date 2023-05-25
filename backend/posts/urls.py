from rest_framework.routers import DefaultRouter
from .views import PostViewset, CommentViewset
# from django.urls import path

router = DefaultRouter(trailing_slash=False)
router.register(r"posts", PostViewset)
router.register(r"comments", CommentViewset)

urlpatterns = [

]

urlpatterns += router.urls