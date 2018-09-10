from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from  django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):

	print("Serializer is working")

	owner = serializers.ReadOnlyField(source='owner.username')
	#owner_id = serializers.IntegerField(source='owner.id')
	#nothing = serializers.CharField(default="nothingnothingnothing")

	class Meta:
		model = Snippet
		#Make sure you also add 'owner', to the list of fields in the inner Meta class.
		#The field 'owner' was declared on serializer SnippetSerializer, but has not been included in the 'fields' option.
		fields = ('id', 'owner_id', 'owner', 'title', 'code', 'linenos', 'language', 'style')


	#id = serializers.IntegerField(read_only=True)
	#title = serializers.CharField(required=False, allow_blank=True, max_length=100)
	#code = serializers.CharField(style={'base_template': 'textarea.html'})
	#linenos = serializers.BooleanField(required=False)
	#language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
	#style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

	# def create(self, validated_data):
	# 	return Snippet.objects.create(**validated_data)

	# def update(self, instance,validated_data):
	# 	"""
	# 	title code linenos language style
	# 	"""
	# 	instance.title = validated_data.get('title', instance.title)
	# 	instance.code = validated_data.get('code', instance.code)
	# 	instance.linenos = validated_data.get('linenos', instance.linenos)
	# 	instance.language = validated_data.get('language', instance.language)
	# 	instance.style = validated_data.get('style', instance.style)
	# 	instance.save()

	# 	return instance
	# 	

class UserSerializer(serializers.ModelSerializer):
	# snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	# not 'snippets-detail'
	# snippets = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='snippet-detail')
	snippets = SnippetSerializer(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')