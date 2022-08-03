import boto3
import troposphere
import troposphere.elasticbeanstalk as beanstalk
import minio


# TODO: Collect details on:
# Beanstalk
# Opensearch
# S3
# ELBv2
# VPC
# Cloudwatch
# Cloudtrail
# KMS
# Route53
# RDS
# Mongo Atlas
# XRay

def get_beanstalk_details():
    beanstalk_session = boto3.session.Session()
    ebs = beanstalk_session.client('elasticbeanstalk')
    return [env["EnvironmentName"] for env in ebs.describe_environments()['Environments']]



def add_beanstalk_to_template(template=troposphere.Template(), beanstalk_specs=[]):
    for spec in beanstalk_specs:
        template.add_resource(beanstalk.Environment())
    pass


def rm_beanstalk_from_template(template):
    pass