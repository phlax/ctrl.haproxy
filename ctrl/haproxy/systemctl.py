
import json
import os

from zope import interface

from ctrl.core.interfaces import IHttpctl


@interface.implementer(IHttpctl)
class Haproxyctl(object):

    async def frontends(self):
        print("getting FRONTENDS in utility: %s" % service)

    async def backends(self):
        print("getting FRONTENDS in utility: %s" % service)

    async def enable(self, service: str):
        print("enabling SERVICE in utility: %s" % service)

    async def disable(self, service: str):
        print("disabling SERVICE in utility: %s" % service)

    async def configure(self):
        print("configuring SERVICES in utility")
