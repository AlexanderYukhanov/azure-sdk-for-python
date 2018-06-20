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


class UpgradeOrchestrationServiceStateSummary(Model):
    """Service state summary of Service Fabric Upgrade Orchestration Service.

    :param current_code_version: The current code version of the cluster.
    :type current_code_version: str
    :param current_manifest_version: The current manifest version of the
     cluster.
    :type current_manifest_version: str
    :param target_code_version: The target code version of  the cluster.
    :type target_code_version: str
    :param target_manifest_version: The target manifest version of the
     cluster.
    :type target_manifest_version: str
    :param pending_upgrade_type: The type of the pending upgrade of the
     cluster.
    :type pending_upgrade_type: str
    """

    _attribute_map = {
        'current_code_version': {'key': 'CurrentCodeVersion', 'type': 'str'},
        'current_manifest_version': {'key': 'CurrentManifestVersion', 'type': 'str'},
        'target_code_version': {'key': 'TargetCodeVersion', 'type': 'str'},
        'target_manifest_version': {'key': 'TargetManifestVersion', 'type': 'str'},
        'pending_upgrade_type': {'key': 'PendingUpgradeType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UpgradeOrchestrationServiceStateSummary, self).__init__(**kwargs)
        self.current_code_version = kwargs.get('current_code_version', None)
        self.current_manifest_version = kwargs.get('current_manifest_version', None)
        self.target_code_version = kwargs.get('target_code_version', None)
        self.target_manifest_version = kwargs.get('target_manifest_version', None)
        self.pending_upgrade_type = kwargs.get('pending_upgrade_type', None)
