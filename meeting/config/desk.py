# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label":_("Tools"),
            "icon": "octicon octicon-briefcase",
            "item": [
                {
                    "type": "doctype",
                    "name": "Meeting",
                    "label": _("Meeting"),
                    "desscrition": _("Prepare agenda, invite users and record minutes"),
                }
            ]
        }
    ]