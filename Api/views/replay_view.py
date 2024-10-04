from .imports import *
from rest_framework.permissions import IsAuthenticated,AllowAny


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reply_list(request):
    """
    List all replys for videos.
    """
    replys = Reply.objects.all()
    paginator = CustomPagination()
    page_obj = paginator.paginate_queryset(replys, request)
    serializer = ReplySerializer(page_obj, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def reply_create(request):
    serializer = ReplySerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def reply_detail(request, pk):
    """
    Retrieve a specific reply by its ID.
    """
    try:
        reply = Reply.objects.get(pk=pk)
        serializer = ReplySerializer(reply)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Reply.DoesNotExist:
        return Response({'errors': 'reply not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def reply_update(request, pk):
    """
    Update a specific reply.
    """
    try:
        reply = Reply.objects.get(pk=pk)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Reply.DoesNotExist:
        return Response({'errors': 'reply not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def reply_delete(request, pk):
    """
    Delete a specific reply.
    """
    try:
        reply = Reply.objects.get(pk=pk)
        reply.delete()
        return Response({'message': 'reply deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Reply.DoesNotExist:
        return Response({'errors': 'reply not found.'}, status=status.HTTP_404_NOT_FOUND)