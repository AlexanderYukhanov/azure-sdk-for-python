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

from .proxy_only_resource import ProxyOnlyResource


class DiagnosticSettingsResource(ProxyOnlyResource):
    """The diagnostic setting resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param storage_account_id: The resource ID of the storage account to which
     you would like to send Diagnostic Logs.
    :type storage_account_id: str
    :param event_hub_authorization_rule_id: The resource Id for the event hub
     authorization rule.
    :type event_hub_authorization_rule_id: str
    :param event_hub_name: The name of the event hub. If none is specified,
     the default event hub will be selected.
    :type event_hub_name: str
    :param metrics: the list of metric settings.
    :type metrics: list[~azure.mgmt.monitor.models.MetricSettings]
    :param logs: the list of logs settings.
    :type logs: list[~azure.mgmt.monitor.models.LogSettings]
    :param workspace_id: The workspace ID (resource ID of a Log Analytics
     workspace) for a Log Analytics workspace to which you would like to send
     Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
    :type workspace_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'event_hub_authorization_rule_id': {'key': 'properties.eventHubAuthorizationRuleId', 'type': 'str'},
        'event_hub_name': {'key': 'properties.eventHubName', 'type': 'str'},
        'metrics': {'key': 'properties.metrics', 'type': '[MetricSettings]'},
        'logs': {'key': 'properties.logs', 'type': '[LogSettings]'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
    }

    def __init__(self, *, storage_account_id: str=None, event_hub_authorization_rule_id: str=None, event_hub_name: str=None, metrics=None, logs=None, workspace_id: str=None, **kwargs) -> None:
        super(DiagnosticSettingsResource, self).__init__(**kwargs)
        self.storage_account_id = storage_account_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.event_hub_name = event_hub_name
        self.metrics = metrics
        self.logs = logs
        self.workspace_id = workspace_id