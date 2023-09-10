from rest_framework import permissions

class IsOwnProfileOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    #This is for the object level permission.
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # # Write permissions are only allowed to the owner of the snippet.
        # return obj.owner == request.user

        #This is for the view level permission.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user