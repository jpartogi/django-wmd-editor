Django WMD Editor
=================


A [WMD-Editor][1] wrapper for Django applications.


Installation
------------

Installing django-wmd-editor should be really as easy as possible. To install
django-wmd-editor all you need to do is just follow these steps:

1. Download and install django-wmd-editor.
    
    You can use `PIP` to install the latest version of django-wmd-editor from github like so:
    
        $ pip install -e git://github.com/marcuswhybrow/django-wmd-editor.git#egg=django_wmd_editor
    
    or you can run `python setup.py install`.

3. Install django-wmd-editor in your django application

        INSTALLED_APPS = (
          ...
          'wmd',
          ...
        )

4. In the `wmd.js` file on line 49, it explicitly states where images are located in your project. By default this is set to `"/static/wmd/images"`, you must change this if your static files are located elsewhere.

    Run `python manage.py collectstatic` to collect the static files in all of your apps (including this one).

5. Add the urls to your `urls.py`:

        urlpatterns = patterns('',
          ...
          (r'^wmd/', include('wmd.urls')),
          ...
        )


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

- `WMD_SHOW_PREVIEW`: Whether to show the preview or not. This is the setting if you use the wmd editor outside the admin.
   Values: True, False
   Default: False
- `WMD_ADMIN_SHOW_PREVIEW`: Whether to show the preview in the admin or not.
   Values: True, False
   Default: True


Bugs & Features request
-----------------------

Just file it in the [issue tracker][3].


License
-------
Copyright &copy; 2009 Scrum8 (<http://scrum8.com>), 2011 Marcus Whybrow under BSD License.


  [1]: http://wmd-editor.com
  [2]: http://github.com/scrum8/django-wmd-editor/downloads
  [3]: http://github.com/scrum8/django-wmd-editor/issues

