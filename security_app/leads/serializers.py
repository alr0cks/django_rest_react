from rest_framework import serializers
from leads.models import Lead

#Lead serializer
class LeadSearilizer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'