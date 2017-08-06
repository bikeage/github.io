#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eliot Logan'
SITENAME = u'skewed'
SITEURL = 'http://bikeage.github.io'
#SITEURL = ''

HEADER_COVER = 'static/my_image.png'
HEADER_COLOR = 'red'

PATH = 'content'

#TIMEZONE = 'Europe/Paris'
TIMEZONE ='US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)



# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/eliotlogan'),
          ('github', 'https://github.com/myprofile'),
          ('Twitter', 'http://twitter.com/eliotlogan'),
          ('envelope','mailto:my@mail.address')
          )

STATIC_PATHS = ['assets']


DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'attila'

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

### Theme specific settings

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "assets/images/avatar.png",
    "image": "assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}
