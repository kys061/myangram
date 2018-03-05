from rest_framework import serializers
from . import models
# from myangram.users import models as user_models


class CommentSerializer(serializers.ModelSerializer):
    # image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    # image = ImageSerializer()

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'id',
            'location',
            'caption',
            'creator',
            'comments',
            'likes'
        )
