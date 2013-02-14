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

from audiofield.forms import CustomerAudioFileForm


class DialerAudioFileForm(CustomerAudioFileForm):

    def __init__(self, *args, **kwargs):
        super(DialerAudioFileForm, self).__init__(*args, **kwargs)
        self.fields['audio_file'].widget.attrs['class'] = "input-file"
