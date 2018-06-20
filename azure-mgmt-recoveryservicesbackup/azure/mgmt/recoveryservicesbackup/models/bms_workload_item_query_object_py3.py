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


class BMSWorkloadItemQueryObject(Model):
    """Filters to list items that can be backed up.

    :param backup_management_type: Backup management type. Possible values
     include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM', 'AzureBackupServer',
     'AzureSql', 'AzureStorage', 'AzureWorkload', 'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param workload_item_type: Workload Item type. Possible values include:
     'Invalid', 'SQLInstance', 'SQLDataBase'
    :type workload_item_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.WorkloadItemType
    :param workload_type: Workload type. Possible values include: 'Invalid',
     'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB', 'Exchange', 'Sharepoint',
     'VMwareVM', 'SystemState', 'Client', 'GenericDataSource', 'SQLDataBase',
     'AzureFileShare'
    :type workload_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.WorkloadType
    :param protection_status: Backup status query parameter. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_status: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    """

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_item_type': {'key': 'workloadItemType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'protection_status': {'key': 'protectionStatus', 'type': 'str'},
    }

    def __init__(self, *, backup_management_type=None, workload_item_type=None, workload_type=None, protection_status=None, **kwargs) -> None:
        super(BMSWorkloadItemQueryObject, self).__init__(**kwargs)
        self.backup_management_type = backup_management_type
        self.workload_item_type = workload_item_type
        self.workload_type = workload_type
        self.protection_status = protection_status
