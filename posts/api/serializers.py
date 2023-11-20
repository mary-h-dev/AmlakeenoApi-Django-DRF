from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from posts.models import Post, Comment, PostLikeDislike



class PostsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()



    def get_like_count(self, obj):
        return PostLikeDislike.objects.filter(post=obj, like=True).count()
    


    def get_dislike_count(self, obj):
        return PostLikeDislike.objects.filter(post=obj, like=False).count()



    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj).order_by('-time')
        serializer = CommentSerializer(comments, many=True)
        return serializer.data
    

    class Meta:
        model = Post
        fields = "__all__"
    


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = "__all__"



class PostLikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikeDislike
        fields = '__all__'
