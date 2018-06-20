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


class SyncGroupSchemaTable(Model):
    """Properties of table in sync group schema.

    :param columns: List of columns in sync group schema.
    :type columns: list[~azure.mgmt.sql.models.SyncGroupSchemaTableColumn]
    :param quoted_name: Quoted name of sync group schema table.
    :type quoted_name: str
    """

    _attribute_map = {
        'columns': {'key': 'columns', 'type': '[SyncGroupSchemaTableColumn]'},
        'quoted_name': {'key': 'quotedName', 'type': 'str'},
    }

    def __init__(self, *, columns=None, quoted_name: str=None, **kwargs) -> None:
        super(SyncGroupSchemaTable, self).__init__(**kwargs)
        self.columns = columns
        self.quoted_name = quoted_name
