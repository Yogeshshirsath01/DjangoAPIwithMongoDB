from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movies
from .serializers import MoviesSerializers

@api_view(['GET','POST','DELETE'])
def movie_list(request):
    if request.method == 'GET':
        movies= Movies.objects.all()
        movies_serializers = MoviesSerializers(movies, many=True)
        return JsonResponse(movies_serializers.data, safe=False)
    elif request.method == 'POST':
        movies_data = JSONParser().parse(request)
        movies_serializers = MoviesSerializers(data=movies_data)
        if movies_serializers.is_valid():
            movies_serializers.save()
            return JsonResponse(movies_serializers.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movies_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Movies.objects.all().delete()
        return JsonResponse({'message': '{} Movies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def movie_detail(request, pk):
    try:
        movies = Movies.objects.get(pk=pk)

        if request.method == 'GET':
            movies_serializers = MoviesSerializers(movies)
            return JsonResponse(movies_serializers.data)
        elif request.method == 'PUT':
            movies_data = JSONParser().parse(request)
            movies_serializers = MoviesSerializers(movies, data=movies_data)
            if movies_serializers.is_valid():
                movies_serializers.save()
                return JsonResponse(movies_serializers.data)
            return JsonResponse(movies_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            movies.delete() 
            return JsonResponse({'message': 'Movie was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except:
        return JsonResponse({'message': 'The Movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
   
