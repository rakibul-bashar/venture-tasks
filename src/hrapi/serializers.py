from .models import Log, Project
from rest_framework.serializers import(
    ModelSerializer,
    ReadOnlyField

)


class LogSerializer(ModelSerializer):
    
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Log
        fields = (
                'id', 'owner','project', 'task_date', 
                'location', 'details', 'working_hour',
                'notes', 'created_at', 'updated_at',
            )


class ProjectSerializer(ModelSerializer):
    
    projects_log = LogSerializer(many=True)
    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'projects_log',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        projects_log = validated_data.pop('projects_log')
        project = Project.objects.create(**validated_data)

        for log in projects_log:
            Log.objects.create(project=project, **log)
        return project

    def update(self, instance, validated_data):
        projects_log = validated_data.pop('projects_log')
        logs = (instance.projects_log).all()
        logs = list(logs)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        for log_data in projects_log:
            log = logs.pop(0)
            log.task_date = log_data.get('task_date', log.task_date)
            log.location = log_data.get('location', log.location)
            log.details = log_data.get('details', log.details)
            log.working_hour = log_data.get('working_hour', log.working_hour)
            log.notes = log_data.get('notes', log.notes)
            log.save()
        return instance