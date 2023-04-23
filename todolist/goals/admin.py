from django.contrib import admin

from todolist.goals.models import Goal, GoalCategory, GoalComment


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated')
    search_fields = ('title', 'user')
    list_filter = ('is_deleted',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'updated', 'category', 'description', 'status', 'priority', 'due_date')
    search_fields = ('title', 'description', 'user')
    list_filter = ('status', 'priority')


@admin.register(GoalComment)
class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ('goal', 'user', 'text', 'created', 'updated')
    search_fields = ('goal', 'text', 'user')
