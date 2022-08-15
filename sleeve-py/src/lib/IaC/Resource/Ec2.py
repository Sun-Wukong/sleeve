import jmespath
import json
import boto3
import boto3.session

def filter_by(key="", operand="==", value=""):
    key_filter = jmespath.compile("?{}{}'{}'".format(key, operand, property))
    return key_filter


def get_security_groups(session=boto3.session.Session(), filters=[]):
    ec2 = session.client('ec2')
    secgroups = ec2.describe_security_groups()
    if len(filters) == 0:
        return json.loads(secgroups)["SecurityGroups"]
    else:
        pass


def get_instances(session=boto3.session.Session()):
    pass


if __name__ == '__main__':
    vpc_filter = filter_by("VpcId", value="vpc-09e1e570")
    sec_grps_by_vpc = jmespath.search(vpc_filter, get_security_groups())
    pass