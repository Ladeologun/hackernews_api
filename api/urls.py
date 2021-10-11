from rest_framework import urlpatterns
from .view.read_view import StoryViewset,CommentViewset
from .view.write_view import CreateStory,StoryDetail,CreateComment,CommentDetail

from rest_framework_nested import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('stories',StoryViewset)
story_router = routers.NestedDefaultRouter(router, 'stories', lookup='story')
story_router.register('comments',CommentViewset,basename="story-comments")

urlpatterns = [
    path(r'',include(router.urls)),
    path(r'',include(story_router.urls)),
    path('addstory/',CreateStory.as_view(),name="add_story"),
    path('addstory/<uuid:id>/',StoryDetail.as_view(),name="update_story"),
    path('addcomment/<uuid:parent>/',CreateComment.as_view(),name="add_comment"),
    path('updatecomment/<uuid:id>/',CommentDetail.as_view(),name="update_comment"),
]
