from rest_framework import serializers

from school_domain.models import Courses


class CoursesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'id',
            'name',
            'code',
            'department',
            'schedule',
            'meta',
            'active'
        )