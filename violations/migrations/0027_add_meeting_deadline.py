# Generated migration for meeting_deadline field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('violations', '0026_add_staff_alert_soft_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffalert',
            name='meeting_deadline',
            field=models.DateTimeField(blank=True, help_text='Deadline for the meeting - expires after this time', null=True),
        ),
    ]
