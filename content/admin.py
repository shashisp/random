from django.contrib import admin
import content.models as models


admin.site.register(models.Content)
admin.site.register(models.Collection)
admin.site.register(models.Vote)
