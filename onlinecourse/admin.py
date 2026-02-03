from django.contrib import admin
# Import all models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Inline classes to edit related models together
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5  # Show 5 extra lesson forms by default

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2  # Show 2 extra choice forms by default

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2  # Show 2 extra question forms by default

# Admin class for Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]  # Add lessons while creating a course
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Admin class for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Add choices while creating a question
    list_display = ['content']  # Show question text in list view

# Admin class for Lesson
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']  # Show lesson title in list view

# Register models with the admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
