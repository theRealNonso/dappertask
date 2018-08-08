from django.conf import settings
from django.core.mail import send_mail
from rest_framework import serializers
import api.models as tm


###############################################################################
# User management and registration
###############################################################################


class AppUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = tm.AppUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def create(self, validated_data):
        appuser = tm.AppUser.objects.create_user(**validated_data)
        return appuser
