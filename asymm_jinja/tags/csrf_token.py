# -*- coding: utf-8 -*-
#    Asymmetric Base Framework :: Jinja utils
#    Copyright (C) 2013-2014 Asymmetric Ventures Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import absolute_import, division, print_function, unicode_literals

from jinja2 import nodes
from jinja2.ext import Extension


class CSRFTokenExtension(Extension):
        tags = set(['csrf_token'])

        def parse(self, parser):
                lineno = parser.stream.next().lineno

                return [nodes.Output(
                        [nodes.TemplateData('<input type="hidden" name="csrfmiddlewaretoken" value="'),
                         nodes.Name('csrf_token', 'load'),
                         nodes.TemplateData('" />'),
                         ]).set_lineno(lineno)]
