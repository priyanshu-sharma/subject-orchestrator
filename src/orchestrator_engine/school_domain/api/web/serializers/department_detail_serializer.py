from rest_framework import serializers

from school_domain.models import Department


class DepartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
            'school',
            'meta',
            'active'
        )