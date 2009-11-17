django-wmd-editor
=================

A `WMD-Editor <http://wmd-editor.com>`_ wrapper for django application.

Installation
============
Installing django-wmd-editor should be really as easy as possible. To install
django-wmd-editor all you need to do is just follow these steps:

1. Get django-wmd-editor
1.1 Checkout django-wmd-editor from github
        ::
        $ git clone git://github.com/scrum8/django-wmd-editor.git

 **Note**: django-wmd-editor have not release a package yet. But we will soon.

2. Install django-wmd-editor package to python site-packages
2.1 Install django-wmd-editor with this command:
        ::
        $ sudo python setup.py install
2.2 Or you can just symlink ~/django-wmd-editor/wmd to your python site packages

3. Install django-wmd-editor in your django application
    ::
    INSTALLED_APPS = (
     ...
     wmd',
     ...
    )

4. Symlink or copy ~/django-wmd-editor/media/wmd directory to where your MEDIA_URL
   directory is pointing to. django-wmd-editor will look for the /wmd path


Usage
=====

* In your models
    ::
    from wmd import models as wmd_models

description = wmd_models.MarkDownField()

* In your forms
    ::
    from wmd.widgets import MarkDownInput

    description = forms.CharField(widget=MarkDownInput())

You also need to add these line on your template to load up the wmd static files:
    ::
    <head>
    {{ form.media }}
    </head>

In the admin, these static files is loaded automatically.


Configuration
=============

In your django settings file, use this configuration for setting up your django wmd editor
* *WMD_OUTPUT*: The format sent to the server.  Use "Markdown" to return the markdown source.
   Values: Markdown, HTML
   Default: Markdown
* *WMD_LINE_LENGTH*: Line wrapping length for lists, blockquotes, etc.
   Default: 40
* *WMD_BUTTONS*: The toolbar buttons.  Undo and redo get appended automatically.
   Values: bold italic link blockquote code image ol ul heading hr |
   Default: bold italic | link blockquote code image | ol ul heading hr
* *WMD_SHOW_PREVIEW*: Whether to show the preview or not. This is the setting if you
   use the wmd editor outside the admin.
   Values: True, False
   Default: False
* *WMD_ADMIN_SHOW_PREVIEW*: Whether to show the preview in the admin or not.
   Values: True, False
   Default: False

Bugs & Features
===============
Just file it in the `issue tracker <http://github.com/scrum8/django-wmd-editor/issues>`_.

License
=======
django-wmd-editor is Copyright © 2009 `Scrum8 <http://scrum8.com>`_ under
BSD License, the same license django is using.