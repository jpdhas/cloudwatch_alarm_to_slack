## Cloudwatch Alarm to Slack Notifier



[![pypi][pypi-image]][pypi-url]
[![pyup][pyup-image]][pyup-url]
[![python-version][python-version-image]][pypi-url]



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

<!-- Markdown links -->

[pypi-image]: https://img.shields.io/pypi/v/cloudwatch-alarm-to-slack.svg
[pypi-url]: https://pypi.python.org/pypi/cloudwatch-alarm-to-slack
[pyup-image]: https://pyup.io/repos/github/jpdhas/cloudwatch_alarm_to_slack/shield.svg
[pyup-url]: https://pyup.io/repos/github/jpdhas/cloudwatch_alarm_to_slack/
[python-version-image]: https://img.shields.io/pypi/pyversions/cloudwatch-alarm-to-slack.svg