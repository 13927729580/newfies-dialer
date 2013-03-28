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
from django.core.exceptions import ObjectDoesNotExist
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.throttle import BaseThrottle
from tastypie.exceptions import NotFound

from dialer_contact.models import Contact, Phonebook
from dialer_campaign.models import Campaign

import logging


logger = logging.getLogger('newfies.filelog')


class CampaignDeleteCascadeResource(ModelResource):
    """

    **Attributes**:

        * ``campaign_id`` - Campaign ID

    **CURL Usage**::

        curl -u username:password --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8000/api/v1/campaign_delete_cascade/%campaign_id%/

    **Example Response**::

        HTTP/1.0 204 NO CONTENT
        Date: Wed, 18 May 2011 13:23:14 GMT
        Server: WSGIServer/0.1 Python/2.6.2
        Vary: Authorization
        Content-Length: 0
        Content-Type: text/plain
    """
    class Meta:
        queryset = Campaign.objects.all()
        resource_name = 'campaign_delete_cascade'
        authorization = Authorization()
        authentication = BasicAuthentication()
        list_allowed_methods = ['delete']
        detail_allowed_methods = ['delete']
        throttle = BaseThrottle(throttle_at=1000, timeframe=3600)

    def obj_delete(self, bundle, **kwargs):
        """
        A ORM-specific implementation of ``obj_delete``.

        Takes optional ``kwargs``, which are used to narrow the query to find
        the instance.
        """
        if not hasattr(bundle.obj, 'delete'):
            try:
                bundle.obj = self.obj_get(bundle=bundle, **kwargs)
            except ObjectDoesNotExist:
                raise NotFound("A model instance matching the provided arguments could not be found.")

        self.authorized_delete_detail(self.get_object_list(bundle.request), bundle)
        del_campaign = bundle.obj

        phonebook_count = del_campaign.phonebook.all().count()
        if phonebook_count > 0:
            other_campaing_count =\
                Campaign.objects.filter(user=bundle.request.user,
                    phonebook__in=del_campaign.phonebook.all())\
                        .exclude(id=del_campaign.id).count()

            if other_campaing_count == 0:
                # delete phonebooks as well as contacts belong to it

                # 1) delete all contacts which are belong to phonebook
                contact_list = Contact.objects\
                    .filter(phonebook__in=del_campaign.phonebook.all())
                contact_list.delete()

                # 2) delete phonebook
                phonebook_list = Phonebook.objects\
                    .filter(id__in=del_campaign.phonebook.all())
                phonebook_list.delete()

        # 3) delete campaign
        bundle.obj.delete()
        logger.debug('CampaignDeleteCascade API : result ok 200')
