#
# ovirt-hosted-engine-setup -- ovirt hosted engine setup
# Copyright (C) 2013-2016 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#


"""hosted engine core plugin."""

from otopi import util

from . import answerfile
from . import conf
from . import misc
from . import preview
from . import shell
from . import titles


@util.export
def createPlugins(context):
    misc.Plugin(context=context)
    conf.Plugin(context=context)
    answerfile.Plugin(context=context)
    preview.Plugin(context=context)
    shell.Plugin(context=context)
    titles.Plugin(context=context)


# vim: expandtab tabstop=4 shiftwidth=4
