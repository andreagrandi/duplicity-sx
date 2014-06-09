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

class SXBackend(duplicity.backend.Backend):
    """Connect to remote store using Skylable Protocol"""
    def __init__(self, parsed_url):
        duplicity.backend.Backend.__init__(self, parsed_url)
        self.parsed_url = parsed_url
        self.url_string = duplicity.backend.strip_auth_from_url(self.parsed_url)

    def _put(self, source_path, remote_filename):
        remote_path = os.path.join(urllib.unquote(self.parsed_url.path.lstrip('/')), 
            remote_filename).rstrip()
        commandline = "sxcp -r {0} {1}".format(source_path.name, remote_path)
        self.subprocess_popen(commandline)

    def _get(self, remote_filename, local_path):
        remote_path = os.path.join(urllib.unquote(self.parsed_url.path), remote_filename).rstrip()
        commandline = "sxcp -r {0} {1}".format(remote_path, local_path.name)
        self.subprocess_popen(commandline)

    def _list(self):
        # Do a long listing to avoid connection reset
        commandline = "sxls -r {0}".format(self.url_string)
        _, l, _ = self.subprocess_popen(commandline)
        # Look for our files as the last element of a long list line
        return [x.split()[-1] for x in l.split('\n') if x and not x.startswith("total ")]

    def _delete(self, filename):
        commandline = "sxrm {0}/{1}".format(self.url_string, filename)
        self.subprocess_popen(commandline)

duplicity.backend.register_backend("sx", SXBackend)
