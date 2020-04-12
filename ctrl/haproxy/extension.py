
from zope import component

from ctrl.core.extension import CtrlExtension
from ctrl.core.interfaces import (
    ICommandRunner, IConfiguration, ICtrlExtension,
    ISubcommand, IHttpctl)

from .command import HaproxySubcommand
from .config import HaproxyConfiguration
from .systemctl import Haproxyctl


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
            Haproxyctl(),
            provides=IHttpctl)


# register the extension
component.provideUtility(
    CtrlHaproxyExtension(),
    ICtrlExtension,
    'haproxy')
