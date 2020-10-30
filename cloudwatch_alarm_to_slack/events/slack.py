"""Module to send a cloudwatch alarm as a message to slack."""

import json
import os

from slack_sdk import WebClient

import cloudwatch_alarm_to_slack.templates.slack as SlackTemplates
import cloudwatch_alarm_to_slack.utils.log as log

LOGGER = log.custom_logger(__name__)


class Slack:
    """Handle interaction with slack."""
    def __init__(self):
        if os.getenv('SLACK_BOT_TOKEN'):
            self.client = WebClient(token=os.getenv('SLACK_BOT_TOKEN'))
        else:
            raise KeyError("SLACK_BOT_TOKEN environment variable not found.")

        if os.getenv('SLACK_CHANNEL'):
            self.slack_channel = os.getenv('SLACK_CHANNEL')
        else:
            raise KeyError("SLACK_CHANNEL environment variable not found.")

    def send_message(self, attachment=None):
        """Sends message to slack."""
        LOGGER.info('Sending message to slack: %s', attachment)
        self.client.chat_postMessage(
            text='*AWS Cloudwatch Notification*',
            attachments=json.dumps(attachment),
            channel=self.slack_channel
        )

    @staticmethod
    def format_message(alarm=None, state=None):
        """Formats cloudwatch alarm details for slack."""
        return SlackTemplates.slack_attachment(
            alarm=alarm,
            state=state
        )
