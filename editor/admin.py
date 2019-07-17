from django.contrib import admin
from django.contrib.auth.models import Group, User
from django import forms
from . import models

admin.site.site_header = 'Net Print'
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(models.WTLHA)
admin.site.register(models.Text)
admin.site.register(models.UpdateRequired)
admin.site.register(models.BascetService)
admin.site.register(models.Section)
admin.site.register(models.Entries)
admin.site.register(models.Page)
admin.site.register(models.ItemPhotoVariant)
admin.site.register(models.ItemPhoto)
admin.site.register(models.ItemBook)
admin.site.register(models.Template)


class JsonChangeForm(forms.ModelForm):
    json = forms.CharField(disabled=False)

    class Meta:
        model = models.Json
        fields = ('name', 'version', 'json')


class JsonAdmin(admin.ModelAdmin):
    form = JsonChangeForm

    def render_change_form(self, request, context, *args, **kwargs):
        self.change_form_template = 'admin/json/json_change_form.html'
        if context['object_id'] is not None:
            obj = models.Json.objects.get(id=context['object_id'])
            extra = {'form': self.form(instance=obj), 'update': '1'}
        else:
            extra = {'form': self.form(), 'update': 0}
        context.update(extra)
        return super(JsonAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(models.Json, JsonAdmin)
