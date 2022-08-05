import boto3
import boto3.session
import troposphere
from troposphere.template_generator import TemplateGenerator
import troposphere.elasticbeanstalk as beanstalk
import minio
import re


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
    envs = ebs.describe_environments()['Environments']
    apps = ebs.describe_applications()['Applications']
    confs = [ebs.describe_configuration_settings(EnvironmentName=env['EnvironmentName'], ApplicationName=env['ApplicationName']) for env in envs] 
    appvs = ebs.describe_application_versions()['ApplicationVersions']

    return {
        "environments": envs,
        "applications": apps,
        "configuration_templates": confs,
        "app_versions": appvs
    }


def build_environment_template(template=troposphere.Template(), environments=[]):
    if len(environments) > 0:
        for env in environments:
            template.add_resource(beanstalk.Environment(
                ApplicationName=env['ApplicationName'],
                CNAMEPrefix=re.sub('(.us-(east|west).[0-9].elasticbeanstalk.com)$','',env['CNAME']),
                EnvironmentName=env['EnvironmentName'],
                PlatformArn=env['PlatformArn'],
                Tier=env['Tier'],
                VersionLabel=env['VersionLabel']
            ))
        return TemplateGenerator(template).to_json()
    else:
        pass


def build_config_template(template=troposphere.Template(), configs=[]):
    if len(configs) > 0:
        for conf in configs:
            template.add_resource(beanstalk.ConfigurationTemplate(
                ApplicationName=conf['ApplicationName'],
                OptionSettings=conf['OptionSettings'],
                PlatformArn=conf['PlatformArn']
            ))
        return TemplateGenerator(template).to_json()
    else:      
        pass


def build_application_template(template=troposphere.Template(), apps=[]):
    if len(apps) > 0:
        for app in apps:
            template.add_resource(beanstalk.Application(
                ApplicationName=app['ApplicationName'],
                ResourceLifecycleConfig=app['ResourceLifecycleConfig']
            ))
        return TemplateGenerator(template).to_json()
    else:
        pass


def build_application_version_template(template=troposphere.Template(), app_vers=[]):
    if len(app_vers) > 0:
        for vers in app_vers:
            template.add_resource(beanstalk.ApplicationVersion(
                ApplicationName=vers['ApplicationName'],
                SourceBundle=app_vers['SourceBundle']
            ))
        return TemplateGenerator(template).to_json()
    else:
        pass