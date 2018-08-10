from django.conf import settings
from rest_framework import serializers
import api.models as dm


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


class JobSerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = dm.Job
        fields = "__all__"
