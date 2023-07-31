from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Students, Courses, Attendance
from .models import AttendanceReport, LeaveReportStaff, LeaveReportStudent, FeedBackStudent,FeedBackStaffs, NotificationStaffs, NotificationStudent


class UserModel(UserAdmin):
    pass 

admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)

