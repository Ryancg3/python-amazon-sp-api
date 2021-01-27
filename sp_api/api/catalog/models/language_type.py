# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LanguageType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'type': 'str',
        'audio_format': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'type': 'Type',
        'audio_format': 'AudioFormat'
    }

    def __init__(self, name=None, type=None, audio_format=None):  # noqa: E501
        """LanguageType - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._audio_format = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if audio_format is not None:
            self.audio_format = audio_format

    @property
    def name(self):
        """Gets the name of this LanguageType.  # noqa: E501

        The name attribute of the item.  # noqa: E501

        :return: The name of this LanguageType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LanguageType.

        The name attribute of the item.  # noqa: E501

        :param name: The name of this LanguageType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this LanguageType.  # noqa: E501

        The type attribute of the item.  # noqa: E501

        :return: The type of this LanguageType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LanguageType.

        The type attribute of the item.  # noqa: E501

        :param type: The type of this LanguageType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def audio_format(self):
        """Gets the audio_format of this LanguageType.  # noqa: E501

        The audio format attribute of the item.  # noqa: E501

        :return: The audio_format of this LanguageType.  # noqa: E501
        :rtype: str
        """
        return self._audio_format

    @audio_format.setter
    def audio_format(self, audio_format):
        """Sets the audio_format of this LanguageType.

        The audio format attribute of the item.  # noqa: E501

        :param audio_format: The audio_format of this LanguageType.  # noqa: E501
        :type: str
        """

        self._audio_format = audio_format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LanguageType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LanguageType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other