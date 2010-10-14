Django WMD Editor
=================


A [WMD-Editor][1] wrapper for django application.


Installation
------------

Installing django-wmd-editor should be really as easy as possible. To install
django-wmd-editor all you need to do is just follow these steps:

1. Get django-wmd-editor

   1.1 Checkout the latest revision of django-wmd-editor from github::

        $ git clone git://github.com/madisona/django-wmd-editor.git

   1.2 Or download the not so latest [django-wmd-editor from github][2]

2. Put django-wmd-editor in your project folder

3. Install django-wmd-editor in your django application::

    INSTALLED_APPS = (
      ...
      wmd',
      ...
    )

4. Symlink or copy `~/django-wmd-editor/media/wmd` directory to where your `MEDIA_URL` directory is pointing to. django-wmd-editor will look for the /wmd path


Usage
-----

1. In your models:

    from wmd import models as wmd_models

    description = wmd_models.MarkDownField()

2. In your forms:

    from wmd.widgets import MarkDownInput

    description = forms.CharField(widget=MarkDownInput())

3. You also need to add these lines on your template to load up the wmd static files:
   
    <head>
    {{ form.media }}
    </head>
   
- In the admin, these static files is loaded automatically.


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
  [2]: http://github.com/madisona/django-wmd-editor/downloads
  [3]: http://github.com/madisona/django-wmd-editor/issues