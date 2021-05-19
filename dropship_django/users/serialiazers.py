from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    stores = serializers.HyperlinkedRelatedField(
        view_name='stores', many=True, read_only=True)
    shoppers = serializers.HyperlinkedRelatedField(
        view_name='shoppers', read_only=True)
    vendors = serializers.HyperlinkedRelatedField(
        view_name='vendors', read_only=True)

    class Meta:
        model = User
        fields = ('__all__', 'stores', 'shoppers', 'vendors')
