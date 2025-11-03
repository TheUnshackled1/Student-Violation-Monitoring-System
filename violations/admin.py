from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import (
	User,
	Student,
	Faculty,
	Staff,
	TemporaryAccessRequest,
	Message,
    Violation,
)


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
	list_display = ("username", "email", "first_name", "last_name", "role", "is_active", "last_login")
	list_filter = ("role", "is_active", "is_staff", "is_superuser")
	search_fields = ("username", "email", "first_name", "last_name")
	readonly_fields = ("created_at",)
	fieldsets = (
		(None, {"fields": ("username", "password")}),
		("Personal info", {"fields": ("first_name", "last_name", "email", "role", "created_at")}),
		(
			"Permissions",
			{
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				)
			},
		),
		("Important dates", {"fields": ("last_login", "date_joined")}),
	)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ("student_id", "user", "program", "year_level", "department", "enrollment_status")
	search_fields = ("student_id", "user__username", "user__first_name", "user__last_name")
	list_filter = ("enrollment_status", "department", "year_level")


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
	list_display = ("employee_id", "user", "position", "office_location")
	search_fields = ("employee_id", "user__username", "user__first_name", "user__last_name")


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
	list_display = ("employee_id", "user", "department", "position", "office_location")
	search_fields = ("employee_id", "user__username", "user__first_name", "user__last_name")
	list_filter = ("department",)


@admin.register(TemporaryAccessRequest)
class TemporaryAccessRequestAdmin(admin.ModelAdmin):
	list_display = ("requester", "status", "duration_hours", "requested_at", "approved_by", "approved_at", "expires_at")
	list_filter = ("status",)
	search_fields = ("requester__username", "approved_by__username")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ("sender", "receiver", "created_at", "read_at")
	search_fields = ("sender__username", "receiver__username", "content")
	list_filter = ("created_at",)


# Register your models here.


@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
	list_display = ("id", "student", "type", "status", "incident_at", "reported_by", "created_at")
	list_filter = ("type", "status", "incident_at", "created_at")
	search_fields = ("student__student_id", "student__user__username", "location", "description")
