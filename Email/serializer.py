from rest_framework import serializers
from .models import Emails

class EmailSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = '__all__'