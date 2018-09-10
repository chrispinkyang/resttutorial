from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

#due to api_view, don't need followings anymore
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# @csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list(request):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets,many=True)
		# return JsonResponse(serializer.data,safe=False)
		return Response(serializer.data)

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			# return JsonResponse(serializer.data,status=201)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			# return JsonResponse(serializer.errors,status=400)
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		# return HttpResponse(status=404)
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		# return JsonResponse(data=serializers.data)
		return Response(serializer.data)

	elif request.method == 'PUT':
		# request.data can handle incoming json requests
		serializer = SnippetSerializer(snippet,data=request.data)
		if serializer.is_valid():
			serializer.save()
			# return JsonResponse(serializer.data)
			return Response(serializer.data)
		else:
			# return JsonResponse(serializer.errors,status=400)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# elif request.method == 'POST':
	# 	data = JSONParser().parse(request)
	# 	serializer = SnippetSerializer(snippet,data=data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		# return JsonResponse(serializer.data)
	# 		return Response(serializer.data)
	# 	else:
	# 		# return JsonResponse(serializer.errors,status=400)
	# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		snippet.delete()
		# return HttpResponse(status=204)
		return Response(status=status.HTTP_204_NO_CONTENT)

