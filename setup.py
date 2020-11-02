#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      author='Jermila Paul Dhas',
      author_email='dhas.jermila@gmail.com',
      python_requires='>=3.6',
      description='A python library to send cloudwatch alarm events from sns to slack',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT license',
      keywords='cloudwatch_alarm_to_slack',
      name='cloudwatch_alarm_to_slack',
      version='0.1',
      url='https://github.com/jpdhas/cloudwatch_alarm_to_slack',
      packages=['cloudwatch_alarm_to_slack'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      zip_safe=False
)
