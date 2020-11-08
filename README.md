## Cloudwatch Alarm to Slack Notifier



[![pypi](https://img.shields.io/pypi/v/cloudwatch-alarm-to-slack.svg)](https://pypi.python.org/pypi/cloudwatch-alarm-to-slack)
[![pyup](https://pyup.io/repos/github/jpdhas/cloudwatch_alarm_to_slack/shield.svg)](https://pyup.io/repos/github/jpdhas/cloudwatch_alarm_to_slack/)



A python library to send cloudwatch alarm notifications to Slack.


## Usage

* Install the package.

```
pip install cloudwatch_alarm_to_slack
```

* It is expected this will be used as a part of a lambda.

```
from cloudwatch_alarm_to_slack.entrypoint import CloudwatchAlarmNotifier

def lambda_handler(event, context):
    CloudwatchAlarmNotifier.handle_event(event)
```

* It is required the following environment variable be set:
    
    - `SLACK_BOT_TOKEN`: Bot token of the slack app which should have the `chat:write` permissions.
    - `SLACK_CHANNEL`: ID of the Slack channel to which notification should be sent to.


------

If there is another usecase, please open an issue and let me know :) 
