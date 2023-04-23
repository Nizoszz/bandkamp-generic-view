from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .pagination import *
from .serializers import SongSerializer
from rest_framework.generics import *


class SongView(ListCreateAPIView, CustomResultPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomResultPagination

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs.get("pk"))