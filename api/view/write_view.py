from rest_framework import status
from api.response import Response
from rest_framework.generics import CreateAPIView,UpdateAPIView,DestroyAPIView
from api.models import Story,Comment
from api.serializers import StorySerializer,AddCommentSerializer


class CreateStory(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDetail(UpdateAPIView,DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    lookup_field = "id"
    error = dict(errors="modification not allowed for stories from hacker news")

    def put(self,request,id):
        story = Story.objects.filter(pk =id).values("item_id")
        itemID = list(story)[0].get("item_id")
        if itemID:
            return Response(errors=self.error,status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().put(request,id)

    def patch(self,request,id):
        story = Story.objects.filter(pk =id).values("item_id")
        itemID = list(story)[0].get("item_id")
        if itemID:
            return Response(errors=self.error,status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().patch(request,id)

    def delete(self,request,id):
        story = Story.objects.filter(pk =id).values("item_id")
        itemID = list(story)[0].get("item_id")
        if itemID:
            return Response(errors=self.error,status=status.HTTP_400_BAD_REQUEST)

        else:
            return super().delete(request,id)

class CreateComment(CreateAPIView):
    serializer_class = AddCommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "parent"

    def get_serializer_context(self):
        return {"parent":self.kwargs["parent"]}


class CommentDetail(UpdateAPIView,DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = AddCommentSerializer
    lookup_field = "id"
    error = dict(errors="modification not allowed for stories from hacker news")

    def put(self,request,id):
        comment = Comment.objects.filter(pk =id).values("item_id")
        itemID = list(comment)[0].get("item_id")
        if itemID:
            return Response(errors=self.error,status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().put(request,id)

    def patch(self,request,id):
        comment = Comment.objects.filter(pk =id).values("item_id")
        itemID = list(comment)[0].get("item_id")
        if itemID:
            return Response(errors=self.error,status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().patch(request,id)

    def delete(self,request,id):
        comment = Comment.objects.filter(pk =id).values("item_id")
        itemID = list(comment)[0].get("item_id")
        if itemID:
            return Response(errors=self.error,status=status.HTTP_400_BAD_REQUEST)

        else:
            return super().delete(request,id)