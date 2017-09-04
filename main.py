#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kytos.core import KytosEvent, KytosNApp, log

class Main(KytosNApp):
    """Main class of a KytosNApp"""

    def setup(self):
        """KytosNApp setup"""

    def execute(self):
        "KytosNApp execute"

        event = KytosEvent(name='viniciusarcanjo/kyslacker.send')
        d = {
            'channel': 'of_notifications',
            'source': '{0}/{1}'.format(self.username, self.name),
            'tag': 'INFO',
            'payload': 'L2circuit X was provisioned for customer A'
        }
        event.content['message'] = d
        log.info('sending message to kyslacker...')
        self.controller.buffers.app.put(event)

    def shutdown(self):
        """Too simple to have a shutdown procedure."""
        pass
