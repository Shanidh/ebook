from rest_framework import serializers
from .models import *

class ebookserialzer(serializers.ModelSerializer):
    class Meta:
        model=Ebook
        fields='__all__'