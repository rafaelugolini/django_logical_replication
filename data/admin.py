import json

from django.contrib import admin

from .models import Data, Annotation


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'data')
    readonly_fields = ('id', 'data')

    def view_data(self, obj):
        return json.dumps(obj.data)


@admin.register(Annotation)
class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'data')
    readonly_fields = ('id', )
    fields = ('data', )

    def view_data(self, obj):
        return json.dumps(obj.data)
