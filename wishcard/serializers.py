from rest_framework import serializers

from .models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        read_only_fields = (
            'created_at',
            'created_by',
        ),
        fields = (
            'id',
            'title',
            'description',
            'created_at',
        )
