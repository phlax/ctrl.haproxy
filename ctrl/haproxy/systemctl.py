
import json
import os

from zope import interface

from ctrl.core.interfaces import IHttpctl


@interface.implementer(IHttpctl)
class Haproxyctl(object):

    async def frontends(self):
        print("getting FRONTENDS in utility")

    async def backends(self):
        print("getting FRONTENDS in utility")

    async def configure(self):
        print("configuring SERVICES in utility")
