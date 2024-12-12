

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.timezone import now
from events.models import Event


User = get_user_model()


class UserSerailizre(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'profile']
        read_only_fields = ['id']



class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    attendees = UserSerailizre(many=True, read_only=True) 

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at','attendees']

        def validate_date(self, value):

        
            if value <= now():
                raise serializers.ValidationError("Event date must be in the future.")
            return value