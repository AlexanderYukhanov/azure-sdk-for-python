# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ValidateProbeInput(Model):
    """Input of the validate probe API.

    All required parameters must be populated in order to send to Azure.

    :param probe_url: Required. The probe URL to validate.
    :type probe_url: str
    """

    _validation = {
        'probe_url': {'required': True},
    }

    _attribute_map = {
        'probe_url': {'key': 'probeURL', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ValidateProbeInput, self).__init__(**kwargs)
        self.probe_url = kwargs.get('probe_url', None)
