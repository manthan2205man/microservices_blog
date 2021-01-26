from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView

from .models import UserTable, Post
from .serializers import BlogPostSerializer
from .authentication import TokenAuthentication


class test(APIView):
    authentication_classes = [TokenAuthentication,]
    # permission_classes = [AdminOrTeacherOnly,]

    def get(self, request, *args,**kwargs):
        # print("USER:", request.user.is_superuser)
        return Response("Success")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def api_blog_post_create(request):
    if request.method=='POST':
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        serializer=BlogPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['author'] = request.user
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def api_blog_post_detail(request,pk):
#     try:
#         post=Post.objects.get(pk=pk)
#     except post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=='GET':
#         serializer=BlogPostSerializer(post)
#         return Response(serializer.data)

# @api_view(['PUT'])
# @authentication_classes(['TokenAuthentication'])
# def api_blog_post_update(request,pk):
#     try:
#         post=Post.objects.get(pk=pk)
#     except post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)



#     if request.method=='PUT':
#         serializer=BlogPostSerializer(post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             publish("post_updated", serializer.data)
#             data={'success':'update succes'}
#             return Response(data=data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# @authentication_classes(['TokenAuthentication'])
# def api_blog_post_delete(request,pk):
#     try:
#         post=Post.objects.get(pk=pk)
#     except post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     user=request.user
#     if post.author!=user:
#         return Response("You don't have permission to delete it.")

#     if request.method=='DELETE':
#         operation=post.delete()
#         if operation:
#             data={'success':'delete success'}
#         else:
#             data={'failure':'delete failed'}
#         return Response(data=data)

