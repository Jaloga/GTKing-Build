#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import xbmc, xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON.openSettings()
