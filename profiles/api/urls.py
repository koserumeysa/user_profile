from django.urls import path, include
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, ProfilePhotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user-profiles', ProfileViewSet)
router.register(r'user-status', ProfileStatusViewSet)
#Instead of these, we can use the above router. And we should update the path as well.
# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_info = ProfileViewSet.as_view({'get': 'retrieve'}) #retrieve is the same as detail

urlpatterns = [
    path('', include(router.urls)),
    path('profile-photo/', ProfilePhotoUpdateView.as_view(), name='profile-photo'),
    #These are for non-router version.
    # path('user-profiles/', profile_list , name='profile-list'),
    # path('user-profils/<int:pk>/', profile_info, name='profile-info'),
]  