import boto3
import boto3.session
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
    envs = ebs.describe_environments()
    apps = ebs.describe_applications()
    confs = [ebs.describe_configuration_settings(EnvironmentName=env['EnvironmentName'], ApplicationName=env['ApplicationName']) for env in envs] 
    appvs = ebs.describe_application_versions()

    return {
        "environments": envs,
        "applications": apps,
        "configuration_templates": confs,
        "app_versions": appvs
    }


def build_environment_template(template=troposphere.Template()):
    pass


def build_config_template(template=troposphere.Template()):
    pass


def build_application_template(template=troposphere.Template()):
    pass


def build_application_version_template(template=troposphere.Template()):
    pass