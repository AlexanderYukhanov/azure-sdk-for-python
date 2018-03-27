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


class SubscriptionUpdateParameters(Model):
    """Subscription update details.

    :param user_id: User identifier path: /users/{uid}
    :type user_id: str
    :param product_id: Product identifier path: /products/{productId}
    :type product_id: str
    :param expiration_date: Subscription expiration date. The setting is for
     audit purposes only and the subscription is not automatically expired. The
     subscription lifecycle can be managed by using the `state` property. The
     date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
     by the ISO 8601 standard.
    :type expiration_date: datetime
    :param display_name: Subscription name.
    :type display_name: str
    :param primary_key: Primary subscription key.
    :type primary_key: str
    :param secondary_key: Secondary subscription key.
    :type secondary_key: str
    :param state: Subscription state. Possible states are * active – the
     subscription is active, * suspended – the subscription is blocked, and the
     subscriber cannot call any APIs of the product, * submitted – the
     subscription request has been made by the developer, but has not yet been
     approved or rejected, * rejected – the subscription request has been
     denied by an administrator, * cancelled – the subscription has been
     cancelled by the developer or administrator, * expired – the subscription
     reached its expiration date and was deactivated. Possible values include:
     'suspended', 'active', 'expired', 'submitted', 'rejected', 'cancelled'
    :type state: str or ~azure.mgmt.apimanagement.models.SubscriptionState
    :param state_comment: Comments describing subscription state change by the
     administrator.
    :type state_comment: str
    """

    _validation = {
        'primary_key': {'max_length': 256, 'min_length': 1},
        'secondary_key': {'max_length': 256, 'min_length': 1},
    }

    _attribute_map = {
        'user_id': {'key': 'properties.userId', 'type': 'str'},
        'product_id': {'key': 'properties.productId', 'type': 'str'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'primary_key': {'key': 'properties.primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'properties.secondaryKey', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'SubscriptionState'},
        'state_comment': {'key': 'properties.stateComment', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubscriptionUpdateParameters, self).__init__(**kwargs)
        self.user_id = kwargs.get('user_id', None)
        self.product_id = kwargs.get('product_id', None)
        self.expiration_date = kwargs.get('expiration_date', None)
        self.display_name = kwargs.get('display_name', None)
        self.primary_key = kwargs.get('primary_key', None)
        self.secondary_key = kwargs.get('secondary_key', None)
        self.state = kwargs.get('state', None)
        self.state_comment = kwargs.get('state_comment', None)