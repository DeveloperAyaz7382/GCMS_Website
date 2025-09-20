from django.contrib import admin

# ============================ Model Imports ============================
from .models import (
    AcademicExcellence, Admission, AdmissionStep, ApplicationDownload,
    ContactInformation, ContactMessage, Department, Event, PrincipalMessage,
    Exam, ExamResult, Facility, FeeStructure, HighlightSection,
    HostelFacility, HostelIntro, LibraryBook, News, PhilosophyBlock, Rule,
    Statistic, Testimonial, FacultyMember, GalleryImage, OnlineApplication, 
)

# ============================ Gallery ============================
admin.site.register(GalleryImage)

# ============================ Event ============================
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'venue']
    search_fields = ['title', 'venue']
    list_filter = ['date']

# ============================ Department ============================
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'degree_type', 'num_of_courses', 'num_of_students', 'slug')
    search_fields = ('name', 'faculty')
    prepopulated_fields = {'slug': ('name',)}

# ============================ Faculty Members ============================
@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'department')
    search_fields = ('name', 'subject', 'department__name')
    list_filter = ('department',)

# ============================ Admission ============================
@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['department', 'program', 'annual_fees', 'duration']
    search_fields = ['department', 'program']

# ============================ Contact Information ============================
@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'facebook_link', 'twitter_link', 'linkedin_link', 'google_plus_link')
    search_fields = ('address', 'phone', 'email')

# ============================ Contact Messages ============================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')

# ============================ Rules ============================
@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ['category', 'visible', 'order', 'created_at']
    list_editable = ['visible', 'order']
    ordering = ['order']

# ============================ Exams ============================
admin.site.register(Exam)
admin.site.register(ExamResult)

# ============================ About Page Static Sections ============================
admin.site.register(PhilosophyBlock)
admin.site.register(Statistic)
admin.site.register(HighlightSection)

# ============================ Admission Process ============================
admin.site.register(AdmissionStep)
admin.site.register(FeeStructure)
admin.site.register(ApplicationDownload)

# ============================ Online Application ============================
@admin.register(OnlineApplication)
class OnlineApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'program', 'previous_institute', 'year_completed', 'created_at')
    search_fields = ('full_name', 'email', 'program', 'previous_institute')
    list_filter = ('program', 'year_completed', 'created_at')
    ordering = ('-created_at',)


# ============================ Facilities & Hostel ============================
admin.site.register(Facility)
admin.site.register(HostelIntro)
admin.site.register(HostelFacility)

# ============================ Library ============================
admin.site.register(LibraryBook)

# ============================ Other General Models ============================
admin.site.register(PrincipalMessage)
admin.site.register(AcademicExcellence)
admin.site.register(Testimonial)
admin.site.register(News)



from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'created_at')
    prepopulated_fields = {'slug': ('title',)}