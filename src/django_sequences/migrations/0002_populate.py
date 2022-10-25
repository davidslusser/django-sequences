# Generated by Django 4.1.2 on 2022-10-25 00:19

from django.db import migrations

def populate_stage_states(apps, schema_editor):
    """ populate StageState values """
    StageState = apps.get_model('django_sequences', 'StageState')
    data_list = [{'name': 'pending', 
                 'description': 'activity on this stage is expected but has not yet started'},
                 {'name': 'started', 
                 'description': 'activity on this stage has started'},
                 {'name': 'completed', 
                 'description': 'activity on this stage has completed'},
                 {'name': 'blocked', 
                 'description': 'activity on this stage is blocked by a previous stage'},
                 ]
    for data in data_list:
        StageState.objects.get_or_create(name=data['name'], description=data['description'], 
        defaults=data)


def populate_stage_results(apps, schema_editor):
    """ populate StageResult values """
    StageResult = apps.get_model('django_sequences', 'StageResult')
    data_list = [{'name': 'success', 
                 'description': 'stage completed successfully with no issues'},
                 {'name': 'fail', 
                 'description': 'stage completed with a well-defined failure condition'},
                 {'name': 'error', 
                 'description': 'stage encountered an error and could not complete'},
                 {'name': 'unknown', 
                 'description': 'stage has not completed, or completion can not be determined'},
                 ]
    for data in data_list:
        StageResult.objects.get_or_create(name=data['name'], description=data['description'], 
        defaults=data)


class Migration(migrations.Migration):

    dependencies = [
        ('django_sequences', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_stage_states),
        migrations.RunPython(populate_stage_results),
    ]
