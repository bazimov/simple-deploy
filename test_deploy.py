"""Unit tests for the script."""
import boto3
from botocore.stub import Stubber

from .deploy import (get_elb_name, get_old_ami_info, launch_new_instances, register_to_elb, terminate_old_instances)


def test_get_ami_info():
    """"""
    client = boto3.client('ec2', region_name='us-east-1')
    stubber = Stubber(client)
    res = {
        'Reservations': [{
            'Groups': [],
            'Instances': [{
                'ImageId': 'ami-88888',
                'InstanceId': 'i-01fb1e7',
                'InstanceType': 'm5.xlarge',
                'KeyName': 'test-key',
                'State': {
                    'Code': 16,
                    'Name': 'running'
                },
                'SubnetId': 'subnet-aaaaaa',
                'VpcId': 'vpc-bbbbb',
                'RootDeviceName': '/dev/xvda',
                'RootDeviceType': 'ebs',
                'SecurityGroups': [{
                    'GroupName': 'launch-wizard-34',
                    'GroupId': 'sg-54444'
                }],
                'Tags': [{
                    'Key': 'Name',
                    'Value': 'messages_logs_parsing_5'
                }],
                'VirtualizationType': 'hvm'
            }],
            'OwnerId':
            '66',
            'ReservationId':
            'r-00665c53a'
        }]
    }
    expected_params = {
        'Filters': [{
            'Name': 'image-id',
            'Values': ['ami-88888']
        }, {
            'Name': 'instance-state-name',
            'Values': ['running']
        }]
    }
    stubber.add_response('describe_instances', res, expected_params)
    with stubber:
        result = get_old_ami_info('ami-88888', client)
        instance_ids = [vm['InstanceId'] for vm in result]

    assert isinstance(result, list)
    assert instance_ids == ['i-01fb1e7']


def test_get_elb_name():
    instance_id = 'i-123455id'
    client = boto3.client('elb', region_name='us-east-1')
    stubber = Stubber(client)
    res = {'LoadBalancerDescriptions': [{'Instances': [{'InstanceId': instance_id}], 'LoadBalancerName': 'test-elb'}]}
    expected_params = {}
    stubber.add_response('describe_load_balancers', res, expected_params)
    with stubber:
        result = get_elb_name([instance_id], client)

    assert isinstance(result, str)
    assert result == 'test-elb'


def test_register_to_elb():
    instance = 'i-123455id'
    client = boto3.client('elb', region_name='us-east-1')
    stubber = Stubber(client)
    res = {
        'Instances': [
            {
                'InstanceId': instance
            },
        ]
    }
    health_res = {
        'InstanceStates': [
            {
                'InstanceId': instance,
                'State': 'InService',
                'ReasonCode': 'string',
                'Description': 'string'
            },
        ]
    }
    expected_params = {'Instances': [{'InstanceId': instance}], 'LoadBalancerName': 'test-elb'}
    stubber.add_response('register_instances_with_load_balancer', res, expected_params)
    stubber.add_response('describe_instance_health', health_res, expected_params)
    with stubber:
        result = register_to_elb('test-elb', [instance], client)

    assert isinstance(result, bool)
    assert result is True
