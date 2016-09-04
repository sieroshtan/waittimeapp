from rest_framework import serializers
from ..models import Wait


class WaitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wait


class WaitRatingPathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wait
        fields = ('rating', 'rating_comment',)
        extra_kwargs = {'rating': {'required': True},
                        'rating_comment': {'required': True}}
