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


class EncryptionDetails(Model):
    """Details needed if the VM was encrypted at the time of backup.

    :param encryption_enabled: Identifies whether this backup copy represents
     an encrypted VM at the time of backup.
    :type encryption_enabled: bool
    :param kek_url: Key Url.
    :type kek_url: str
    :param secret_key_url: Secret Url.
    :type secret_key_url: str
    :param kek_vault_id: ID of Key Vault where KEK is stored.
    :type kek_vault_id: str
    :param secret_key_vault_id: ID of Key Vault where Secret is stored.
    :type secret_key_vault_id: str
    """

    _attribute_map = {
        'encryption_enabled': {'key': 'encryptionEnabled', 'type': 'bool'},
        'kek_url': {'key': 'kekUrl', 'type': 'str'},
        'secret_key_url': {'key': 'secretKeyUrl', 'type': 'str'},
        'kek_vault_id': {'key': 'kekVaultId', 'type': 'str'},
        'secret_key_vault_id': {'key': 'secretKeyVaultId', 'type': 'str'},
    }

    def __init__(self, *, encryption_enabled: bool=None, kek_url: str=None, secret_key_url: str=None, kek_vault_id: str=None, secret_key_vault_id: str=None, **kwargs) -> None:
        super(EncryptionDetails, self).__init__(**kwargs)
        self.encryption_enabled = encryption_enabled
        self.kek_url = kek_url
        self.secret_key_url = secret_key_url
        self.kek_vault_id = kek_vault_id
        self.secret_key_vault_id = secret_key_vault_id
