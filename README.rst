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


Bugs & Features
===============
Just file it in the `issue tracker <http://github.com/scrum8/django-wmd-editor/issues>`_.

License
=======
django-wmd-editor is Copyright © 2009 `Scrum8 <http://scrum8.com>`_ under BSD License, the same license django is using.