#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.utils.translation import gettext as _
from apiplayground import APIPlayground


class CampaignAPIPlayground(APIPlayground):

    schema = {
        "title": _("campaign"),
        "base_url": "http://localhost/api/v1/",
        "resources": [
            {
                "name": "/campaign/",
                "description": _("this resource allows you to manage campaign."),
                "endpoints": [
                    {
                        "method": "GET",
                        "url": "/api/v1/campaign/",
                        "description": _("returns all campaigns")
                    },
                    {
                        "method": "GET",
                        "url": "/api/v1/campaign/{campaign-id}/",
                        "description": _("returns a specific campaign")
                    },
                    {
                        "method": "POST",
                        "url": "/api/v1/campaign/",
                        "description": _("create new campaign"),
                        "parameters": [
                            {
                                "name": "name",
                                "type": "string",
                                "is_required": True,
                                "default": "Sample Campaign"
                            },
                            {
                                "name": "description",
                                "type": "string"
                            },
                            {
                                "name": "callerid",
                                "type": "string"
                            },
                            {
                                "name": "caller_name",
                                "type": "string"
                            },
                            {
                                "name": "startingdate",
                                "type": "string",
                                "default": "1301392136.0"
                            },
                            {
                                "name": "expirationdate",
                                "type": "string",
                                "default": "1301332136.0"
                            },
                            {
                                "name": "frequency",
                                "type": "string",
                                "default": "20"
                            },
                            {
                                "name": "callmaxduration",
                                "type": "string",
                                "default": "50"
                            },
                            {
                                "name": "maxretry",
                                "type": "string",
                                "default": "3"
                            },
                            {
                                "name": "intervalretry",
                                "type": "string",
                                "default": "300"
                            },
                            {
                                "name": "completion_maxretry",
                                "type": "string",
                                "default": "0"
                            },
                            {
                                "name": "completion_intervalretry",
                                "type": "string",
                                "default": "900"
                            },
                            {
                                "name": "calltimeout",
                                "type": "string",
                                "default": "45"
                            },
                            {
                                "name": "aleg_gateway",
                                "type": "string",
                                "default": "1"
                            },
                            {
                                "name": "content_type",
                                "type": "string",
                                "default": "survey_template"
                            },
                            {
                                "name": "object_id",
                                "type": "string",
                                "default": "1"
                            },
                            {
                                "name": "extra_data",
                                "type": "string",
                                "default": "2000"
                            },
                            {
                                "name": "phonebook_id",
                                "type": "string",
                                "default": "1"
                            },
                        ]
                    },
                    {
                        "method": "PATCH",
                        "url": "/api/v1/campaign/{campaign-id}/",
                        "description": _("update campaign"),
                        "parameters": [
                            {
                                "name": "name",
                                "type": "string",
                                "is_required": True,
                                "default": "Sample Campaign"
                            },
                            {
                                "name": "description",
                                "type": "string"
                            },
                            {
                                "name": "callerid",
                                "type": "string"
                            },
                            {
                                "name": "caller_name",
                                "type": "string"
                            },
                            {
                                "name": "startingdate",
                                "type": "string",
                                "default": "1301392136.0"
                            },
                            {
                                "name": "expirationdate",
                                "type": "string",
                                "default": "1301332136.0"
                            },
                            {
                                "name": "frequency",
                                "type": "string",
                                "default": "20"
                            },
                            {
                                "name": "callmaxduration",
                                "type": "string",
                                "default": "50"
                            },
                            {
                                "name": "maxretry",
                                "type": "string",
                                "default": "3"
                            },
                            {
                                "name": "intervalretry",
                                "type": "string",
                                "default": "3000"
                            },
                            {
                                "name": "calltimeout",
                                "type": "string",
                                "default": "45"
                            },
                            {
                                "name": "aleg_gateway",
                                "type": "string",
                                "default": "1"
                            },
                            {
                                "name": "content_type",
                                "type": "string",
                                "default": "survey_template"
                            },
                            {
                                "name": "object_id",
                                "type": "string",
                                "default": "1"
                            },
                            {
                                "name": "extra_data",
                                "type": "string",
                                "default": "2000"
                            },
                            {
                                "name": "phonebook_id",
                                "type": "string",
                                "default": "1"
                            },
                        ]
                    },
                    {
                        "method": "DELETE",
                        "url": "/api/v1/campaign/{campaign-id}/",
                        "description": _("delete campaign"),
                    }
                ]
            }
        ]
    }
