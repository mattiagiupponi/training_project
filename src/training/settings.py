# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import ast

from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen, Request
# Load more settings from a file called local_settings.py if it exists
try:
    from training.local_settings import *
#    from geonode.local_settings import *
except ImportError:
    from geonode.settings import *

#
# General Django development settings
#
PROJECT_NAME = "training"

# add trailing slash to site url. geoserver url will be relative to this
if not SITEURL.endswith("/"):
    SITEURL = "{}/".format(SITEURL)

SITENAME = os.getenv("SITENAME", "training")

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "en")

if PROJECT_NAME not in INSTALLED_APPS:
    INSTALLED_APPS += (PROJECT_NAME,)

# Location of url mappings
ROOT_URLCONF = os.getenv("ROOT_URLCONF", "{}.urls".format(PROJECT_NAME))

# Additional directories which hold static files
# - Give priority to local geonode-project ones
STATICFILES_DIRS = [
    os.path.join(LOCAL_ROOT, "static"),
] + STATICFILES_DIRS

# Location of locale files
LOCALE_PATHS = (os.path.join(LOCAL_ROOT, "locale"),) + LOCALE_PATHS

TEMPLATES[0]["DIRS"].insert(0, os.path.join(LOCAL_ROOT, "templates"))
loaders = TEMPLATES[0]["OPTIONS"].get("loaders") or [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]["OPTIONS"]["loaders"] = loaders
TEMPLATES[0].pop("APP_DIRS", None)

INSTALLED_APPS += ("training.custom",)

INSTALLED_APPS += ("training.example",)

LANGUAGES = (
    ('en-us', 'English'),
    ('it-it', 'Italiano'),
)

MAPSTORE_TRANSLATIONS_PATH = [
    '/static/mapstore/ms-translations',
    '/static/mapstore/gn-translations',
    '/static/mapstore/project-translations'
]

DEFAULT_MAP_CENTER_X = 1261620 # initial x center position of the map (EPSG:3857 default crs)
DEFAULT_MAP_CENTER_Y = 5439686 # initial y center position of the map (EPSG:3857 default crs)
DEFAULT_MAP_ZOOM = 10 # initial zoom level of the map

MAPSTORE_BASELAYERS = [
    {
        "type": "osm",
        "title": "Open Street Map",
        "name": "mapnik",
        "source": "osm",
        "group": "background",
        "visibility": True
    },
    {
        "source": "ol",
        "group": "background",
        "id": "none",
        "name": "empty",
        "title": "Empty Background",
        "type": "empty",
        "visibility": False,
        "args": ["Empty Background", {"visibility": False}]
    },
    {
        "format": "image/jpeg",
        "group": "background",
        "name": "osm:osm_simple_dark",
        "opacity": 1,
        "title": "OSM Simple Dark",
        "thumbURL": "/static/img/hero.jpeg",
        "type": "wms",
        "url": [
            "https://maps6.geosolutionsgroup.com/geoserver/wms",
            "https://maps3.geosolutionsgroup.com/geoserver/wms",
            "https://maps1.geosolutionsgroup.com/geoserver/wms",
            "https://maps4.geosolutionsgroup.com/geoserver/wms",
            "https://maps2.geosolutionsgroup.com/geoserver/wms",
            "https://maps5.geosolutionsgroup.com/geoserver/wms"
        ],
        "source": "osm_simple_dark",
        "visibility": False,
        "singleTile": False,
        "credits": {
            "title": "OSM Simple Dark | Rendering <a href=\"https://www.geo-solutions.it/\">GeoSolutions</a> | Data © <a href=\"http://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"http://www.openstreetmap.org/copyright\">ODbL</a>"
        }
    }
]