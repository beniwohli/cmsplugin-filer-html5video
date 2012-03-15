# -*- coding: utf-8 -*-

from django.conf import settings

VIDEO_WIDTH = getattr(settings, "VIDEO_WIDTH", 320)
VIDEO_HEIGHT = getattr(settings, "VIDEO_HEIGHT", 240)

VIDEO_AUTOPLAY = getattr(settings, "VIDEO_AUTOPLAY", False)
VIDEO_AUTOHIDE = getattr(settings, "VIDEO_AUTOHIDE", False)
VIDEO_FULLSCREEN = getattr(settings, "VIDEO_FULLSCREEN", True)
VIDEO_LOOP = getattr(settings, "VIDEO_LOOP", False)
