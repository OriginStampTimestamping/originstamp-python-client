# coding: utf-8

"""
    OriginStamp Client

    OpenAPI spec version: 3.0
    OriginStamp Documentation: https://doc.originstamp.org
    Contact: mail@originstamp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ProofRequest(object):
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
        'hash_string': 'str',
        'proof_type': 'int'
    }

    attribute_map = {
        'currency': 'currency',
        'hash_string': 'hash_string',
        'proof_type': 'proof_type'
    }

    def __init__(self, currency=None, hash_string=None, proof_type=None):  # noqa: E501
        """ProofRequest - a model defined in Swagger"""  # noqa: E501

        self._currency = None
        self._hash_string = None
        self._proof_type = None
        self.discriminator = None

        self.currency = currency
        self.hash_string = hash_string
        self.proof_type = proof_type

    @property
    def currency(self):
        """Gets the currency of this ProofRequest.  # noqa: E501

        0: Bitcoin  # noqa: E501

        :return: The currency of this ProofRequest.  # noqa: E501
        :rtype: int
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ProofRequest.

        0: Bitcoin  # noqa: E501

        :param currency: The currency of this ProofRequest.  # noqa: E501
        :type: int
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def hash_string(self):
        """Gets the hash_string of this ProofRequest.  # noqa: E501

        Hash in HEX representation for which the proof should be created. We allow the use of SHA-256. Note: We handle the hashes in lower-case.  # noqa: E501

        :return: The hash_string of this ProofRequest.  # noqa: E501
        :rtype: str
        """
        return self._hash_string

    @hash_string.setter
    def hash_string(self, hash_string):
        """Sets the hash_string of this ProofRequest.

        Hash in HEX representation for which the proof should be created. We allow the use of SHA-256. Note: We handle the hashes in lower-case.  # noqa: E501

        :param hash_string: The hash_string of this ProofRequest.  # noqa: E501
        :type: str
        """
        if hash_string is None:
            raise ValueError("Invalid value for `hash_string`, must not be `None`")  # noqa: E501

        self._hash_string = hash_string

    @property
    def proof_type(self):
        """Gets the proof_type of this ProofRequest.  # noqa: E501

        Specifies which type of file should be returned. Possible value(s):  0: proof with a seed file (txt) or proof with a merkle tree (xml) 1: proof with a PDF file   Other formats will follow.  # noqa: E501

        :return: The proof_type of this ProofRequest.  # noqa: E501
        :rtype: int
        """
        return self._proof_type

    @proof_type.setter
    def proof_type(self, proof_type):
        """Sets the proof_type of this ProofRequest.

        Specifies which type of file should be returned. Possible value(s):  0: proof with a seed file (txt) or proof with a merkle tree (xml) 1: proof with a PDF file   Other formats will follow.  # noqa: E501

        :param proof_type: The proof_type of this ProofRequest.  # noqa: E501
        :type: int
        """
        if proof_type is None:
            raise ValueError("Invalid value for `proof_type`, must not be `None`")  # noqa: E501

        self._proof_type = proof_type

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProofRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
