from pipes import Template
import boto3
import boto3.session
import troposphere
from troposphere.template_generator import TemplateGenerator
import troposphere.ec2 as ec2


def get_vpc_details():
    vpc_session = boto3.session.Session()
    sess = vpc_session.client(ec2)
    vpcs = sess.describe_vpcs()
    return vpcs


def build_vpc_template(template=Template(), vpcs=[]):
    if len(vpcs) > 0:
        for vpc in vpcs:
            template.add_resource(ec2.VPC(
                CidrBlock=vpc['CidrBlock']
            ))
    return TemplateGenerator(template).to_json()
