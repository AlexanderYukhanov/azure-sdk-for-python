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


class ProtectionIntent(Model):
    """Base class for backup ProtectionIntent.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureResourceProtectionIntent

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup managemenent for the backed
     up item. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param source_resource_id: ARM ID of the resource to be backed up.
    :type source_resource_id: str
    :param item_id: ID of the item which is getting protected, In case of
     Azure Vm , it is ProtectedItemId
    :type item_id: str
    :param policy_id: ID of the backup policy with which this item is backed
     up.
    :type policy_id: str
    :param protection_state: Backup state of this backup item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param protection_intent_item_type: Required. Constant filled by server.
    :type protection_intent_item_type: str
    """

    _validation = {
        'protection_intent_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'policy_id': {'key': 'policyId', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'protection_intent_item_type': {'key': 'protectionIntentItemType', 'type': 'str'},
    }

    _subtype_map = {
        'protection_intent_item_type': {'AzureResourceItem': 'AzureResourceProtectionIntent'}
    }

    def __init__(self, **kwargs):
        super(ProtectionIntent, self).__init__(**kwargs)
        self.backup_management_type = kwargs.get('backup_management_type', None)
        self.source_resource_id = kwargs.get('source_resource_id', None)
        self.item_id = kwargs.get('item_id', None)
        self.policy_id = kwargs.get('policy_id', None)
        self.protection_state = kwargs.get('protection_state', None)
        self.protection_intent_item_type = None
