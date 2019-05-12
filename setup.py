# coding: utf-8

"""
    OriginStamp Client

    OpenAPI spec version: 3.0
    OriginStamp Documentation: https://doc.originstamp.org
    Contact: mail@originstamp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "originstamp-client"
VERSION = "1.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "numpy >= 1.15.4"]

setup(
    name=NAME,
    version=VERSION,
    description="OriginStamp Client",
    author_email="mail@originstamp.com",
    url="https://originstamp.com",
    keywords=["Swagger", "OriginStamp Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Python client for the trusted timestamping service OriginStamp, see https://github.com/OriginStampTimestamping/originstamp-client-python.
    """
)
