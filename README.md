Django WMD Editor
=================


A [WMD-Editor][1] wrapper for django application.


Installation
------------

Installing django-wmd-editor should be really as easy as possible. To install
django-wmd-editor all you need to do is just follow these steps:

1. Get django-wmd-editor
    
    1.1 pip install the lates version of django-wmd-editor from github
    
        $ pip install -e git://github.com/marcuswhybrow/django-wmd-editor.git#egg=django_wmd_editor

3. Install django-wmd-editor in your django application

    INSTALLED_APPS = (
      ...
      'wmd',
      ...
    )

4. In the wmd.js file on line 49, it explicitly states where images are located in your project. By default this is set to "/static/wmd/images", you must change this if your static files are located elsewhere.

    4.1 Run `python manage.py collectstatic` to collate the static files in all of your apps (including this one).


Usage
-----

1. In your models

    from wmd import models as wmd_models

    description = wmd_models.MarkDownField()

2. In your forms

    from wmd.widgets import MarkDownInput

    description = forms.CharField(widget=MarkDownInput())

3. You also need to add these lines on your template to load the wmd static files.
   
    <head>
    {{ form.media }}
    </head>
   
- In the admin, these static files are loaded automatically.


Configuration
-------------

In your django settings file, use this configuration for setting up your django wmd editor

- **WMD_SHOW_PREVIEW**: Whether to show the preview or not. This is the setting if you
   use the wmd editor outside the admin.
   Values: True, False
   Default: False
- **WMD_ADMIN_SHOW_PREVIEW**: Whether to show the preview in the admin or not.
   Values: True, False
   Default: True


Bugs & Features request
-----------------------

Just file it in the [issue tracker][3].


License
-------
Copyright (c) 2009 Scrum8 (http://scrum8.com) under BSD License.


  [1]: http://wmd-editor.com
  [3]: http://github.com/marcuswhybrow/django-wmd-editor/issues
