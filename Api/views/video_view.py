# views.py

from .imports import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.conf import settings

@api_view(['GET'])
@permission_classes([AllowAny])
def video_list(request):
    videos = Video.objects.all().order_by('-created_at')
    # paginator = CustomPagination()
    # page_obj = paginator.paginate_queryset(videos, request)
    serializer = VideoSerializer(videos, many=True)
    # return paginator.get_paginated_response(serializer.data)
    return Response({'results': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def video_create(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def video_detail(request, pk):
    try:
        video = Video.objects.get(pk=pk)
        video_url = request.build_absolute_uri(settings.MEDIA_URL + str(video.video_file))
        return Response({
            'id': video.id,
            'created_at': video.created_at,
            'name': video.name,
            'description': video.description,
            'video_file': video_url,
            'category': video.category.id,
            'user':video.user.name,
        })
    except Video.DoesNotExist:
        return Response({"errors": "Video not found."}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def video_update(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return Response({"errors": "Video not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = VideoSerializer(video, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def video_delete(request, pk):
    try:
        video = Video.objects.get(pk=pk)
        video.delete()
        return Response({"message": "Video deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Video.DoesNotExist:
        return Response({"errors": "Video not found."}, status=status.HTTP_404_NOT_FOUND)
