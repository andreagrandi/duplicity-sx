# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2014 Andrea Grandi <a.grandi@gmail.com>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import os.path
import urllib

import duplicity.backend
from duplicity import globals
from duplicity import log
from duplicity import tempdir

class SXBackend(duplicity.backend.Backend):
    """Connect to remote store using Skylable Protocol"""
    def __init__(self, parsed_url):
        pass

    def _put(self, source_path, remote_filename):
        pass

    def _get(self, remote_filename, local_path):
        pass

    def _list(self):
        pass

    def _delete(self, filename):
        pass

duplicity.backend.register_backend("sx", SXBackend)
