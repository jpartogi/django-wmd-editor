# $Id: models.py 5f79ec26972e 2009/08/15 06:22:28 jpartogi $ 

from django.db import models
from django.contrib.admin import widgets as admin_widgets
from djangowmd import widgets

class MarkDownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': forms.Textarea}
        defaults.update(kwargs)
        return super(TextField, self).formfield(**defaults)
    