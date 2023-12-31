from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfilePhotoSerializer
from profiles.api.permissions import IsOwnProfileOrReadOnly, StatusOwnerOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet

class ProfileViewSet(
            mixins.ListModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]

    filter_backends = [SearchFilter]
    search_fields = ['location', 'user__username']

class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, StatusOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset
    
    #This will get the user_id and realize the operations.
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)

class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [IsAuthenticated] 

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object