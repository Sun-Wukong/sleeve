import boto3
import boto3.session
import troposphere
import troposphere.route53 as route53
from troposphere.template_generator import TemplateGenerator


def get_hosted_zone_details(session=boto3.session.Session()):
    r53 = session.client(route53)
    hosted_zones = r53.list_hosted_zones()['HostedZones']
    return hosted_zones


def get_recordset_groups(session=boto3.session.Session(), hosted_zones=get_hosted_zone_details()):
    r53 = session.client(route53)
    recordset_groups = [
        {
            'Id': zone['Id'],
            'ZoneName': zone['Name'],
            'RecordSets': r53.list_resource_record_sets(Id=zone['Id'])['ResourceRecordSets']
        } for zone in hosted_zones
    ]
    return recordset_groups


def get_health_check_confs():
    pass


def make_health_check():
    pass


def build_hosted_zone_templates(template=troposphere.Template(), zones=[]):
    if len(zones) > 1:
        for zone in zones:
            template.add_resource(route53.HostedZone(
                Name=zone['Name']
            ))
        yield TemplateGenerator(template).to_json()
    elif len(zones) == 1:
        template.add_resource(route53.HostedZone(
            Name=zone[0]['Name']
        ))
        return TemplateGenerator(template).to_yaml()
    else:
        pass


def build_record_set_group_templates(template=troposphere.Template(), rec_set_grps=[]):
    if len(rec_set_grps) > 1:
        for rsg in rec_set_grps:
            template.add_resource(route53.RecordSetGroup(
                HostedZoneName=rsg['ZoneName'],
                Recordsets=rsg['RecordSets']
            ))
            yield TemplateGenerator(template).to_yaml()
    elif len(rec_set_grps) == 1:
        template.add_resource(route53.RecordSetGroup(
            HostedZoneName=rec_set_grps[0]['ZoneName'],
            RecordSets=rec_set_grps[0]['RecordSets']
        ))
        return TemplateGenerator(template).to_yaml()
    else:
        pass


def build_health_check_templates(template=troposphere.Template(), check_confs=[]):
    pass
