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

from django.urls import re_path
from geonode.urls import urlpatterns
from training.example.views import insert_custom, serve_training

"""
# You can register your own urlpatterns here
urlpatterns = [
    url(r'^/?$',
        homepage,
        name='home'),
 ] + urlpatterns
"""
urlpatterns = [
    re_path(r'^training/$',
        serve_training,
        name='training'),
    re_path(r'^insert_custom/$',
        insert_custom,
        name='insert_custom'),
 ] + urlpatterns
