#!/usr/bin/env python3
"""Simple AWS Deploy script.

   Provide currently running old AMI id and new AMI id to deploy.
   Example: deploy ami-12334 ami-23445

   TODO:
       1. Add feat AutoScaling Groups.
       2. Extract/add resource tags too.
       3. Extract/add instance profile too.
       5. Could convert to paginate for larger batches.
"""
import boto3

from .utils import (argument_parser, get_elb_name, get_old_ami_info,
                    launch_new_instances, register_to_elb,
                    terminate_old_instances)


def main():
    """Simple deployment script."""
    old_image, new_image = argument_parser()

    ec2_client = boto3.client('ec2', region_name='us-east-1')
    elb_client = boto3.client('elb', region_name='us-east-1')

    currently_running = get_old_ami_info(image=old_image, client=ec2_client)
    old_instance_ids = [vm['InstanceId'] for vm in currently_running]
    load_balancer_name = get_elb_name(instances=old_instance_ids, client=elb_client)
    new_instances = launch_new_instances(image=new_image, data=currently_running, client=ec2_client)
    register_instances = register_to_elb(lb_name=load_balancer_name, instances=new_instances, client=elb_client)

    if register_instances:
        terminate_old_instances(
            lb_name=load_balancer_name, instances=old_instance_ids, client_ec2=ec2_client, client_elb=elb_client)


if __name__ == '__main__':
    main()
