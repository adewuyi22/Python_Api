from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
#from dataclasses import field
from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Link
        fields = "__all__"


        