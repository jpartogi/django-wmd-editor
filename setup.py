# $Id: setup.py d4ce2551f91d 2009/08/22 13:00:06 jpartogi $
#!/usr/bin/env python

from distutils.core import setup

app_name = 'wmd'

setup(name='django-%s-editor' % app_name,
        version='0.9.0',
        packages=[app_name, '%s.templatetags' % app_name],
        package_data = {app_name: ['templates/wmd.*', 'templates/wmd/*.js', 'templates/wmd/images/*.png']},
        author = 'Joshua Partogi',
        author_email = 'joshua.partogi@gmail.com',
        url = 'http://bitbucket.org/scrum8/django-wmd-editor/',
        download_url = 'http://bitbucket.org/scrum8/django-wmd-editor/downloads/',

        license = "BSD License",
        keywords = "django wmd editor",
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        platforms = ['any'],
)
