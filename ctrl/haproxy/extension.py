
from zope import component

from ctrl.core.extension import CtrlExtension
from ctrl.core.interfaces import (
    ICommandRunner, IConfiguration, ICtrlExtension,
    ISubcommand, ISystemctl)

from .command import HaproxySubcommand
from .config import HaproxyConfiguration
from .systemctl import HaproxySystemctl


class CtrlHaproxyExtension(CtrlExtension):

    def register_adapters(self):
        component.provideAdapter(
            factory=HaproxySubcommand,
            adapts=[ICommandRunner],
            provides=ISubcommand,
            name='haproxy')

    async def register_utilities(self):
        component.provideUtility(
            HaproxyConfiguration(),
            provides=IConfiguration,
            name='haproxy')
        component.provideUtility(
            HaproxySystemctl(),
            provides=ISystemctl)


# register the extension
component.provideUtility(
    CtrlHaproxyExtension(),
    ICtrlExtension,
    'haproxy')
