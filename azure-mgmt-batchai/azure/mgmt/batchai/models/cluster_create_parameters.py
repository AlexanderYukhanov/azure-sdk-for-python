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


class ClusterCreateParameters(Model):
    """Cluster creation operation.

    All required parameters must be populated in order to send to Azure.

    :param vm_size: Required. VM size. The size of the virtual machines in the
     cluster. All nodes in a cluster have the same VM size. For information
     about available VM sizes for clusters using images from the Virtual
     Machines Marketplace see Sizes for Virtual Machines (Linux). Batch AI
     service supports all Azure VM sizes except STANDARD_A0 and those with
     premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
    :type vm_size: str
    :param vm_priority: VM priority. VM priority. Allowed values are:
     dedicated (default) and lowpriority. Possible values include: 'dedicated',
     'lowpriority'. Default value: "dedicated" .
    :type vm_priority: str or ~azure.mgmt.batchai.models.VmPriority
    :param scale_settings: Scale settings. Scale settings for the cluster.
     Batch AI service supports manual and auto scale clusters.
    :type scale_settings: ~azure.mgmt.batchai.models.ScaleSettings
    :param virtual_machine_configuration: VM configuration. OS image
     configuration for cluster nodes. All nodes in a cluster have the same OS
     image.
    :type virtual_machine_configuration:
     ~azure.mgmt.batchai.models.VirtualMachineConfiguration
    :param node_setup: Node setup. Setup to be performed on each compute node
     in the cluster.
    :type node_setup: ~azure.mgmt.batchai.models.NodeSetup
    :param user_account_settings: Required. User account settings. Settings
     for an administrator user account that will be created on each compute
     node in the cluster.
    :type user_account_settings:
     ~azure.mgmt.batchai.models.UserAccountSettings
    :param subnet: Subnet. Existing virtual network subnet to put the cluster
     nodes in. Note, if a File Server mount configured in node setup, the File
     Server's subnet will be used automatically.
    :type subnet: ~azure.mgmt.batchai.models.ResourceId
    """

    _validation = {
        'vm_size': {'required': True},
        'user_account_settings': {'required': True},
    }

    _attribute_map = {
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'vm_priority': {'key': 'properties.vmPriority', 'type': 'VmPriority'},
        'scale_settings': {'key': 'properties.scaleSettings', 'type': 'ScaleSettings'},
        'virtual_machine_configuration': {'key': 'properties.virtualMachineConfiguration', 'type': 'VirtualMachineConfiguration'},
        'node_setup': {'key': 'properties.nodeSetup', 'type': 'NodeSetup'},
        'user_account_settings': {'key': 'properties.userAccountSettings', 'type': 'UserAccountSettings'},
        'subnet': {'key': 'properties.subnet', 'type': 'ResourceId'},
    }

    def __init__(self, **kwargs):
        super(ClusterCreateParameters, self).__init__(**kwargs)
        self.vm_size = kwargs.get('vm_size', None)
        self.vm_priority = kwargs.get('vm_priority', "dedicated")
        self.scale_settings = kwargs.get('scale_settings', None)
        self.virtual_machine_configuration = kwargs.get('virtual_machine_configuration', None)
        self.node_setup = kwargs.get('node_setup', None)
        self.user_account_settings = kwargs.get('user_account_settings', None)
        self.subnet = kwargs.get('subnet', None)
