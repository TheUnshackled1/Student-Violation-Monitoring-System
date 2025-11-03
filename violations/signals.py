from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, Student, Faculty, Staff


@receiver(post_save, sender=User)
def create_role_profile(sender, instance: User, created: bool, **kwargs):
    if not created:
        return
    # Auto-create a matching role profile for convenience
    if instance.role == User.Role.STUDENT:
        Student.objects.create(user=instance, student_id=f"{instance.username}")
    elif instance.role == User.Role.FACULTY_ADMIN:
        Faculty.objects.create(user=instance, employee_id=f"FAC-{instance.username}")
    elif instance.role == User.Role.STAFF:
        Staff.objects.create(user=instance, employee_id=f"STA-{instance.username}")
