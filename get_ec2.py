# -*- coding: utf-8 -*-

import boto3
import sys 
from pprint import pprint 

def lambda_handler(event, context): 
    ec2 = boto3.resource('ec2')

    try:
        # 起動中のインスタンス取得	
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        pprint(instances)
    except Exception, e:
        print(e)
        sys.exit(2)


    if not instances is None:
        i = []
        for instance in instances:
            i.append(instance.instance_id)
    else:
        print("not found running instances")
        sys.exit(0)

    return i

    sys.exit(0)
