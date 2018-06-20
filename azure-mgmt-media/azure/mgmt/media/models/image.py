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

from .video import Video


class Image(Video):
    """Describes the basic properties for generating thumbnails from the input
    video.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: JpgImage, PngImage

    All required parameters must be populated in order to send to Azure.

    :param label: An optional label for the codec. The label can be used to
     control muxing behavior.
    :type label: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param key_frame_interval: The distance between two key frames, thereby
     defining a group of pictures (GOP). The value should be a non-zero integer
     in the range [1, 30] seconds, specified in ISO 8601 format. The default is
     2 seconds (PT2S).
    :type key_frame_interval: timedelta
    :param stretch_mode: The resizing mode - how the input video will be
     resized to fit the desired output resolution(s). Default is AutoSize.
     Possible values include: 'None', 'AutoSize', 'AutoFit'
    :type stretch_mode: str or ~azure.mgmt.media.models.StretchMode
    :param start: The position in the input video from where to start
     generating thumbnails. The value can be in absolute timestamp (ISO 8601,
     e.g: PT05S), or a frame count (For example, 10 for the 10th frame), or a
     relative value (For example, 1%). Also supports a macro {Best}, which
     tells the encoder to select the best thumbnail from the first few seconds
     of the video.
    :type start: str
    :param step: The intervals at which thumbnails are generated. The value
     can be in absolute timestamp (ISO 8601, e.g: PT05S for one image every 5
     seconds), or a frame count (For example, 30 for every 30 frames), or a
     relative value (For example, 1%).
    :type step: str
    :param range: The position in the input video at which to stop generating
     thumbnails. The value can be in absolute timestamp (ISO 8601, e.g: PT5M30S
     to stop at 5 minutes and 30 seconds), or a frame count (For example, 300
     to stop at the 300th frame), or a relative value (For example, 100%).
    :type range: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'key_frame_interval': {'key': 'keyFrameInterval', 'type': 'duration'},
        'stretch_mode': {'key': 'stretchMode', 'type': 'StretchMode'},
        'start': {'key': 'start', 'type': 'str'},
        'step': {'key': 'step', 'type': 'str'},
        'range': {'key': 'range', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'#Microsoft.Media.JpgImage': 'JpgImage', '#Microsoft.Media.PngImage': 'PngImage'}
    }

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        self.step = kwargs.get('step', None)
        self.range = kwargs.get('range', None)
        self.odatatype = '#Microsoft.Media.Image'
