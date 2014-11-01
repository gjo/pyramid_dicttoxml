# -*- coding: utf-8 -*-

import dicttoxml


def xml_renderer_factory(info):
    def renderer(value, system):
        request = system.get('request')
        if request is not None:
            response = request.response
            content_type = response.content_type
            if content_type == response.default_content_type:
                response.content_type = 'text/xml'
        #custom_root = value.pop('custom_root', None)
        xml = dicttoxml.dicttoxml(value, attr_type=False, root=False)
        return xml
    return renderer


def includeme(config):
    config.add_renderer('dicttoxml', xml_renderer_factory)
