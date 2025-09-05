#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Georgi Zhelyazkov'
SITENAME = 'Manofash'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme settings
THEME = 'theme'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/logo.png': {'path': 'logo.png'},
    'extra/favicons/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicons/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicons/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicons/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/favicons/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/favicons/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extra/favicons/site.webmanifest': {'path': 'site.webmanifest'},
}

# Custom settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
