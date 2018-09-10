from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework.decorators import action
from rest_framework import generics
from rest_framework import permissions

from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User
#from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
		})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `highlight` action.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	#filter_backends = (DjangoFilterBackend,)
	filter_fields = ('owner_id',)

	#if u r Authenticated, u can post
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	permission_classes = (permissions.AllowAny,)
	
	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	@action(methods=['post'], detail=False)
	def some_thing(self, request, *args, **kwargs):
		return Response(request.data)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
