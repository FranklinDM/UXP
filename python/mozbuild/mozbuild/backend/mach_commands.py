# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import, print_function, unicode_literals

import argparse
import os
import sys
import subprocess
import which

from mozbuild.base import (
    MachCommandBase,
)

from mach.decorators import (
    CommandArgument,
    CommandProvider,
    Command,
)

@CommandProvider
class MachCommands(MachCommandBase):
    @Command('ide', category='devenv',
        description='Generate a project and launch an IDE.')
    @CommandArgument('ide', choices=['visualstudio'])
    @CommandArgument('args', nargs=argparse.REMAINDER)
    def eclipse(self, ide, args):
        if ide == 'visualstudio':
            backend = 'VisualStudio'

        # Here we refresh the whole build. 'build export' is sufficient here and is probably more
        # correct but it's also nice having a single target to get a fully built and indexed
        # project (gives a easy target to use before go out to lunch).
        res = self._mach_context.commands.dispatch('build', self._mach_context)
        if res != 0:
            return 1

        # Generate or refresh the IDE backend.
        python = self.virtualenv_manager.python_path
        config_status = os.path.join(self.topobjdir, 'config.status')
        args = [python, config_status, '--backend=%s' % backend]
        res = self._run_command_in_objdir(args=args, pass_thru=True, ensure_exit_code=False)
        if res != 0:
            return 1


        if ide == 'visualstudio':
            visual_studio_workspace_dir = self.get_visualstudio_workspace_path()
            process = subprocess.check_call(['explorer.exe', visual_studio_workspace_dir])

    def get_visualstudio_workspace_path(self):
        return os.path.join(self.topobjdir, 'msvc', 'mozilla.sln')
