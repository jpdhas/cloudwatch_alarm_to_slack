#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

setup(
      author='Jermila Paul Dhas',
      author_email='dhas.jermila@gmail.com',
      python_requires='>=3.6',
      description='Module to send cloudwatch alarm events from sns to slack',
      install_requires=requirements,
      license='MIT license',
      keywords='cloudwatch_alarm_to_slack',
      name='cloudwatch_alarm_to_slack',
      version='0.1',
      url='http://github.com/storborg/funniest',
      packages=['cloudwatch_alarm_to_slack'],
      zip_safe=False
)
