# $Id: models.py 6d33f21c6e8a 2009/08/15 06:33:15 jpartogi $ 

from django.db import models
from django.contrib.admin import widgets as admin_widgets
from wmd import widgets as wmd_widgets

class MarkDownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'widget': wmd_widgets.MarkDownInput}
        defaults.update(kwargs)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = wmd_widgets.AdminMarkDownInput

    return super(TextField, self).formfield(**defaults)
    