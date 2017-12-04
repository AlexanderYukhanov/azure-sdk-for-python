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


class UpdateImageList(Model):
    """Update Image List Response.

    :param id: Id of the image list.
    :type id: float
    :param name: Name of the image list.
    :type name: str
    :param description: Description of the image list.
    :type description: str
    :param metadata: Metadata of the image list.
    :type metadata:
     ~azure.cognitiveservices.vision.contentmoderator.models.UpdateImageListMetadata
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'float'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': 'UpdateImageListMetadata'},
    }

    def __init__(self, id=None, name=None, description=None, metadata=None):
        self.id = id
        self.name = name
        self.description = description
        self.metadata = metadata