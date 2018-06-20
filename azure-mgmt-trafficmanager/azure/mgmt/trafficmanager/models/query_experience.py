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


class QueryExperience(Model):
    """Class representing a Traffic Manager HeatMap query experience properties.

    All required parameters must be populated in order to send to Azure.

    :param endpoint_id: Required. The id of the endpoint from the 'endpoints'
     array which these queries were routed to.
    :type endpoint_id: int
    :param query_count: Required. The number of queries originating from this
     location.
    :type query_count: int
    :param latency: The latency experienced by queries originating from this
     location.
    :type latency: float
    """

    _validation = {
        'endpoint_id': {'required': True},
        'query_count': {'required': True},
    }

    _attribute_map = {
        'endpoint_id': {'key': 'endpointId', 'type': 'int'},
        'query_count': {'key': 'queryCount', 'type': 'int'},
        'latency': {'key': 'latency', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(QueryExperience, self).__init__(**kwargs)
        self.endpoint_id = kwargs.get('endpoint_id', None)
        self.query_count = kwargs.get('query_count', None)
        self.latency = kwargs.get('latency', None)
