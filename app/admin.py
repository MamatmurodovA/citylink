from django.contrib import admin

from app.models import Survey, ServiceRank, Service


class ServiceInlineAdmin(admin.TabularInline):
    model = ServiceRank
    fields = ('service', 'rank', )


class SurveyAdmin(admin.ModelAdmin):
    inlines = (ServiceInlineAdmin, )


admin.site.register(Survey, SurveyAdmin)
admin.site.register(ServiceRank)
admin.site.register(Service)