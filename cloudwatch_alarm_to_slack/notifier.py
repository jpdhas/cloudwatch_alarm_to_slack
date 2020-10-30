"""Module to send message to Slack when a cloudwatch alarm triggers."""
import json
import sys

from cloudwatch_alarm_to_slack.events.cloudwatch import CloudwatchAlarm

import cloudwatch_alarm_to_slack.utils.log as log
LOGGER = log.custom_logger(__name__)


def handle_event(event):
    """Receive Cloudwatch alarm notification from SNS."""

    message = json.loads(event['Records'][0]['Sns']['Message'])

    LOGGER.info('Processing event: %s', message)
    CloudwatchAlarm.process_alarm(alarm=message)
