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


class RestoreRequest(Model):
    """Base class for restore request. Workload-specific restore requests are
    derived from this class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureFileShareRestoreRequest, AzureWorkloadRestoreRequest,
    IaasVMRestoreRequest

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
    }

    _subtype_map = {
        'object_type': {'AzureFileShareRestoreRequest': 'AzureFileShareRestoreRequest', 'AzureWorkloadRestoreRequest': 'AzureWorkloadRestoreRequest', 'IaasVMRestoreRequest': 'IaasVMRestoreRequest'}
    }

    def __init__(self, **kwargs):
        super(RestoreRequest, self).__init__(**kwargs)
        self.object_type = None
