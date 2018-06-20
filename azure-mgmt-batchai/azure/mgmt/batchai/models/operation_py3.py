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


class Operation(Model):
    """A REST API operation.

    Details of a REST API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The operation name. This is of the format
     {provider}/{resource}/{operation}
    :vartype name: str
    :param display: The object that describes the operation.
    :type display: ~azure.mgmt.batchai.models.OperationDisplay
    :ivar origin: The intended executor of the operation.
    :vartype origin: str
    :param properties: Properties of the operation.
    :type properties: object
    """

    _validation = {
        'name': {'readonly': True},
        'origin': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, display=None, properties=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display
        self.origin = None
        self.properties = properties
