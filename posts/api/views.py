from posts.models import Post, Comment, PostLikeDislike
from .serializers import CommentSerializer, PostsSerializer, PostLikeDislikeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)
        data = serializer.data

        for post_data in data:
            post = Post.objects.get(id=post_data["id"])
            post_data["like_count"] = PostLikeDislike.objects.filter(
                post=post, like=True
            ).count()
            post_data["dislike_count"] = PostLikeDislike.objects.filter(
                post=post, like=False
            ).count()

            if request.user.is_authenticated:
                user_like = PostLikeDislike.objects.filter(
                    user=request.user, post=post
                ).first()
                if user_like:
                    post_data["user_like"] = user_like.like
                else:
                    post_data["user_like"] = None
            else:
                post_data["user_like"] = None

        return Response(data)


# class PostDetail(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        if request.user.is_authenticated:
            user_like = instance.likes.filter(user=request.user).first()
            if user_like:
                data["user_like"] = user_like.like
            else:
                data["user_like"] = None
        else:
            data["user_like"] = None

        return Response(data)


# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostsSerializer(posts, many=True)
#         data = serializer.data

#         for post_data in data:
#             post = Post.objects.get(id=post_data["id"])
#             post_data["like_count"] = post.likes.filter(like=True).count()
#             post_data["dislike_count"] = post.likes.filter(like=False).count()

#             if request.user.is_authenticated:
#                 user_like = post.likes.filter(user=request.user).first()
#                 if user_like:
#                     post_data["user_like"] = user_like.like
#                 else:
#                     post_data["user_like"] = None
#             else:
#                 post_data["user_like"] = None

#         return Response(data)


# class PostDetail(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostsSerializer




class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeDislikeList(generics.ListAPIView):
    queryset = PostLikeDislike.objects.all()
    serializer_class = PostLikeDislikeSerializer


class LikeDislikeCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user
        like_dislike_value = request.data.get("like_dislike")

        # Check if the user has already liked/disliked the post
        like_dislike = PostLikeDislike.objects.filter(post=post, user=user).first()

        if like_dislike:
            # If the user has already liked/disliked the post, update the like_dislike value
            like_dislike.like = like_dislike_value
            like_dislike.save()
        else:
            # If the user has not liked/disliked the post, create a new like_dislike object
            like_dislike = PostLikeDislike.objects.create(
                post=post, user=user, like=like_dislike_value
            )

        return Response(status=status.HTTP_200_OK)
