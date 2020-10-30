"""Module to send message to Slack when a cloudwatch alarm triggers."""
import json

import cloudwatch_alarm_to_slack.utils.log as log
from cloudwatch_alarm_to_slack.events.cloudwatch import CloudwatchAlarm

LOGGER = log.custom_logger(__name__)


def handle_event(event):
    """Receive Cloudwatch alarm notification from SNS."""
    message = json.loads(event['Records'][0]['Sns']['Message'])

    LOGGER.info('Processing event: %s', message)
    CloudwatchAlarm.process_alarm(alarm=message)
