from .imports import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def category_videos(request, pk):
    category = get_object_or_404(Category, pk=pk)
    videos = Video.objects.filter(category=category)
    video_list = list(videos.values())
    return JsonResponse({'results': video_list}, safe=False)

@api_view(['GET'])
@permission_classes([AllowAny])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        # paginator = CustomPagination()
        # page_obj = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(categories, many=True)
        # return paginator.get_paginated_response(serializer.data)
        return Response({'results': serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"errors": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def category_update(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"errors": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({"message": "Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({"errors": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
