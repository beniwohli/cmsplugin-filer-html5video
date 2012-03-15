# -*- coding: utf-8 -*-

import os

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from filer.settings import FILER_STATICMEDIA_PREFIX

from cmsplugin_filer_html5video.models import FilerHTML5Video

class FilerHTML5VideoPlugin(CMSPluginBase):
    model = FilerHTML5Video
    name = _("HTML5 Video (Filer)")

    render_template = "cmsplugin_filer_html5video/video.html"
    text_enabled = True

    general_fields = [
        'title',
        ('width', 'height'),
        'auto_play',
        'auto_hide',
        'fullscreen',
        'loop',
        ]

    fieldsets = [
        (None, {
            'fields': general_fields,
        }),
        (_('formats'), {
            'fields': ('video_mp4', 'video_webm', 'video_ogv', 'image')
        })
    ]

    def render(self, context, instance, placeholder):
        formats = {}
        for format in ('video_mp4', 'video_webm', 'video_ogv'):
            if getattr(instance, format + '_id'):
                formats[format.replace('_', '/')] = getattr(instance, format).url
        context.update({
            'object': instance,
            'placeholder':placeholder,
            'formats': formats
        })
        return context

    def icon_src(self, instance):
        return os.path.normpath(u"%s/icons/video_%sx%s.png" % (FILER_STATICMEDIA_PREFIX, 32, 32,))

plugin_pool.register_plugin(FilerHTML5VideoPlugin)