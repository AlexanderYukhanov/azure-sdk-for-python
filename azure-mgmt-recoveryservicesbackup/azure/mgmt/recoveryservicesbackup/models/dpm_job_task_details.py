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


class DpmJobTaskDetails(Model):
    """DPM workload-specific job task details.

    :param task_id: The task display name.
    :type task_id: str
    :param start_time: The start time.
    :type start_time: datetime
    :param end_time: The end time.
    :type end_time: datetime
    :param duration: Time elapsed for task.
    :type duration: timedelta
    :param status: The status.
    :type status: str
    """

    _attribute_map = {
        'task_id': {'key': 'taskId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'duration': {'key': 'duration', 'type': 'duration'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DpmJobTaskDetails, self).__init__(**kwargs)
        self.task_id = kwargs.get('task_id', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.duration = kwargs.get('duration', None)
        self.status = kwargs.get('status', None)
