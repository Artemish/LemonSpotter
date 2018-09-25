import os
import json
import datetime
import logging

from gajim.plugins import GajimPlugin

from gajim.common import configpaths
from gajim.common import app
from gajim.common import ged

log = logging.getLogger('gajim.plugin_system.birthday')

TITLE = _('%s has birthday today')
TEXT = _('Send him a message')


class BirthDayPlugin(GajimPlugin):
    def init(self):
        self.config_dialog = None
        self.description = ('Dardles spotter')

        self.events_handlers = {
            'presence-received': (ged.GUI2, self._presence_received)
            }

        self.timeout_id = None
        self._timeout_id_start = None

        self.showed_accounts = []

        self._birthdays = {}
        self._load_birthdays()

    def activate(self):
        pass

    def deactivate(self):
        pass

    def _load_peeps(self):
        pass

    def _presence_received(self, event):
        print(event)
        return

    def _find_contact(self, jid):
        accounts = app.contacts.get_accounts()
        for account in accounts:
            contact = app.contacts.get_contacts(account, jid)
            if contact is not None:
                return account, contact[0]
