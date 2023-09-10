from rest_framework import serializers
from profiles.models import Profile, ProfileStatus

class ProfileSerializer(serializers.ModelSerializer):
    #we want to show the name of the user, not the id.
    user = serializers.StringRelatedField(read_only=True)
    #we want to save different endpoints for photos.
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['photo',]


class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = '__all__' 