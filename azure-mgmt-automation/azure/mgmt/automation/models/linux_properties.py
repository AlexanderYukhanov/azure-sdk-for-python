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


class LinuxProperties(Model):
    """Linux specific update configuration.

    :param included_package_classifications: Update classifications included
     in the software update configuration. Possible values include:
     'Unclassified', 'Critical', 'Security', 'Other'
    :type included_package_classifications: str or
     ~azure.mgmt.automation.models.LinuxUpdateClasses
    :param excluded_package_name_masks: packages excluded from the software
     update configuration.
    :type excluded_package_name_masks: list[str]
    :param included_package_name_masks: packages included from the software
     update configuration.
    :type included_package_name_masks: list[str]
    """

    _attribute_map = {
        'included_package_classifications': {'key': 'includedPackageClassifications', 'type': 'str'},
        'excluded_package_name_masks': {'key': 'excludedPackageNameMasks', 'type': '[str]'},
        'included_package_name_masks': {'key': 'includedPackageNameMasks', 'type': '[str]'},
    }

    def __init__(self, included_package_classifications=None, excluded_package_name_masks=None, included_package_name_masks=None):
        super(LinuxProperties, self).__init__()
        self.included_package_classifications = included_package_classifications
        self.excluded_package_name_masks = excluded_package_name_masks
        self.included_package_name_masks = included_package_name_masks