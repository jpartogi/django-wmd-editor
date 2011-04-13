#!/usr/bin/env python

from distutils.core import setup

app_name = 'wmd'

setup(name='django-%s-editor' % app_name,
        version='0.9.0',
        packages=[app_name],
        package_data = {app_name: ['static/wmd/*.js', 'static/wmd/*.css', 'static/wmd/images/*.png']},
        author = 'Joshua Partogi',
        author_email = 'joshua.partogi@gmail.com',
        url = 'http://github.com/marcuswhybrow/django-wmd-editor/',
        download_url = 'http://github.com/marcuswhybrow/django-wmd-editor/archives/master/',

        license = "BSD License",
        keywords = "django wmd editor",
        classifiers = [
            'Development Status :: 3 - Alpha',
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
