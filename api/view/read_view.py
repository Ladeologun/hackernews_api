from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from api.models import Story,Comment
from api.pagination import DefaultPagination
from bin.service import Service
from api.filters import StoryFilter
from api.serializers import StorySerializer,CommentSerializer


class StoryViewset(ReadOnlyModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = StoryFilter
    pagination_class = DefaultPagination
    search_fields = ["title"]
    service = Service()

    def save_items_data(self):
        res = self.service.getstories()
        if res is not None:
            try:
                story_item = res[0:10]
                for storyID in story_item:
                    story_exist = Story.objects.filter(item_id=storyID).exists()
                    if not story_exist:
                        res_story = self.service.getstory(storyID)
                        if res_story is not None:
                            new_story = Story.objects.create(author=res_story.get("by"),descendants=res_story.get("descendants"),score=res_story.get("score"),
                            title=res_story.get("title"),url=res_story.get("url"),time=res_story.get("time"),item_id=res_story.get("id"),type=res_story.get("type")
                            )
                            comment_item = res_story["kids"]
                            for commentID in comment_item:
                                comment_data = self.service.getcomment(commentID)
                                if comment_data is not None:
                                    new_comment = Comment.objects.create(author=comment_data.get("by"),parent=new_story,
                                    text=comment_data.get("text"),time=comment_data.get("time"),item_id=comment_data.get("id"))
            except Exception as error:
                print(error)
                return error


class CommentViewset(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent=self.kwargs['story_pk'])