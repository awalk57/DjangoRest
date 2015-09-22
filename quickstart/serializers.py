from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Urls
        fields = ('url', 'url_text')

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Applications
        fields = ('url','application_name' )