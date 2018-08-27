#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Naomi See'
SITENAME = 'Naomi did a thing'
SITEURL = 'https://seenaomi.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

THEME ='html5-dopetrope'
PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python Meetup', 'https://www.meetup.com/Omahas-Python-Users-Group/'),
         ('Python Meetup on Twitter', 'https://twitter.com/OmahaPython'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/colorful_n0mi'),
          ('Github', 'https://github.com/seenaomi'),
          ('Instagram', 'https://www.instagram.com/seemenaomi/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_METADATA = {
    'status': 'draft',
}

LOAD_CONTENT_CACHE = False