# coding: utf-8

"""
    OriginStamp Client

    OpenAPI spec version: 3.0
    OriginStamp Documentation: https://docs.originstamp.com
    Contact: mail@originstamp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class WebhookRequest(object):
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
        'currency': 'int',
        'hash': 'str',
        'target': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'hash': 'hash',
        'target': 'target'
    }

    def __init__(self, currency=None, hash=None, target=None):  # noqa: E501
        """WebhookRequest - a model defined in Swagger"""  # noqa: E501

        self._currency = None
        self._hash = None
        self._target = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if hash is not None:
            self.hash = hash
        if target is not None:
            self.target = target

    @property
    def currency(self):
        """Gets the currency of this WebhookRequest.  # noqa: E501

        Currency ID for which the webhook should be executed. Possible values: 0: Bitcoin 1: Ethereum 2: AION 100: Südkurier  # noqa: E501

        :return: The currency of this WebhookRequest.  # noqa: E501
        :rtype: int
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this WebhookRequest.

        Currency ID for which the webhook should be executed. Possible values: 0: Bitcoin 1: Ethereum 2: AION 100: Südkurier  # noqa: E501

        :param currency: The currency of this WebhookRequest.  # noqa: E501
        :type: int
        """

        self._currency = currency

    @property
    def hash(self):
        """Gets the hash of this WebhookRequest.  # noqa: E501

        Hash (SHA-256 in HEX) for which a notification is requested.  # noqa: E501

        :return: The hash of this WebhookRequest.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this WebhookRequest.

        Hash (SHA-256 in HEX) for which a notification is requested.  # noqa: E501

        :param hash: The hash of this WebhookRequest.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def target(self):
        """Gets the target of this WebhookRequest.  # noqa: E501

        Target address to which a POST request should be executed.  # noqa: E501

        :return: The target of this WebhookRequest.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this WebhookRequest.

        Target address to which a POST request should be executed.  # noqa: E501

        :param target: The target of this WebhookRequest.  # noqa: E501
        :type: str
        """

        self._target = target

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
        if issubclass(WebhookRequest, dict):
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
        if not isinstance(other, WebhookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
