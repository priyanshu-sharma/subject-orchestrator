from rest_framework import serializers

from school_domain.models import Schools


class SchoolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = (
            'id',
            'name',
            'state',
            'country',
            'college_name',
            'type',
            'meta',
            'active'
        )