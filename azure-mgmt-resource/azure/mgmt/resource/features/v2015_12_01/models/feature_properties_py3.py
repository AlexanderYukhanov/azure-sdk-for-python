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


class FeatureProperties(Model):
    """Information about feature.

    :param state: The registration state of the feature for the subscription.
    :type state: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, *, state: str=None, **kwargs) -> None:
        super(FeatureProperties, self).__init__(**kwargs)
        self.state = state
