"""Test for cloudwatch_alarm_to_slack/notifier."""

from unittest import mock

from cloudwatch_alarm_to_slack.notifier import handle_event


@mock.patch('cloudwatch_alarm_to_slack.events.cloudwatch.CloudwatchAlarm.process_alarm')
def test_cloudwatch_alarm_process_alarm(mock_cloudwatch_alarm):
    """Test if cloudwatch alarm is processsed for a valid event."""

    mock_cloudwatch_event = {
        'Records': [
            {
                'Sns': {
                    'Type': 'Notification',
                    'Subject': 'test_subject',
                    'Message': '{"AlarmName":"test_alarm","AlarmDescription":"test_description","AWSAccountId":"test_account","NewStateValue":"ALARM","Region":"US West (Oregon)","OldStateValue":"INSUFFICIENT_DATA","Trigger":{"MetricName":"Invocations","Namespace":"test_service","StatisticType":"Statistic","Statistic":"SUM","Period":60,"EvaluationPeriods":1,"ComparisonOperator":"LessThanOrEqualToThreshold","Threshold":0.0}}'
                }
            }
        ]
    }

    handle_event(mock_cloudwatch_event)
    mock_message = {
        'AlarmName': 'test_alarm',
        'AlarmDescription': 'test_description',
        'AWSAccountId': 'test_account',
        'NewStateValue': 'ALARM',
        'Region': 'US West (Oregon)',
        'OldStateValue': 'INSUFFICIENT_DATA',
        'Trigger': {
            'MetricName': 'Invocations',
            'Namespace': 'test_service',
            'StatisticType': 'Statistic',
            'Statistic': 'SUM',
            'Period': 60,
            'EvaluationPeriods': 1,
            'ComparisonOperator': 'LessThanOrEqualToThreshold',
            'Threshold': 0.0
        }
    }
    mock_cloudwatch_alarm.assert_called_once_with(alarm=mock_message)
