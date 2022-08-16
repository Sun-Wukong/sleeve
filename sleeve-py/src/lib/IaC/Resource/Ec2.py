import jmespath
import json
import boto3
import boto3.session

def filter_by(key="", operand="==", value="", options={}):
    if options != None:
        return jmespath.compile("?{}{}'{}'".format(options["key"], options["operand"], options["value"]))
    else:
        return jmespath.compile("?{}{}'{}'".format(key, operand, value))


def get_security_groups(session=boto3.session.Session(), filters=[]):
    ec2 = session.client('ec2')
    secgroups = ec2.describe_security_groups()
    if len(filters) == 0:
        return json.loads(secgroups)["SecurityGroups"]
    elif type(filters[0]) == str:
        if len(filters == 3):
            return [json.loads(result) for result in jmespath.search(filter_by(
                key=filters[0],
                operand=filters[1],
                value=filters[-1]
        ),secgroups)]
        else:
            return [json.loads(result) for result in jmespath.search(filter_by(
                key=filters[0],
                value=filters[-1]
            ),secgroups)]
    else:
        results = {}
        for item in filters:
            results["by_{}".format(item["key"])] = [sg for sg in jmespath.search(filter_by(
                options=item
            ),secgroups)]
        pass


def get_instances(session=boto3.session.Session()):
    pass


if __name__ == '__main__':
    vpc_filter = filter_by("VpcId", value="vpc-09e1e570")
    sec_grps_by_vpc = jmespath.search(vpc_filter, get_security_groups())
    pass