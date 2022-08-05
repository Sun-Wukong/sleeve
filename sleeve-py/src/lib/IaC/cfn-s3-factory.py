import boto3
import boto3.session
import troposphere
import troposphere.s3 as s3
from troposphere.template_generator import TemplateGenerator
import minio
import re


def get_s3_details():
    s3_session = boto3.session.Session()
    s3 = s3_session.client('s3')
    buckets = s3.list_buckets()
    bucket_names = [bucket['Name'] for bucket in buckets]
    try:
        cors_policies = [s3.get_bucket_cors(Bucket=bucket) for bucket in bucket_names]
    except:
        print("Unsuccessful")
    return {
        "buckets": buckets,
        "cors": cors_policies
    }


def build_bucket_template(template=troposphere.Template(), buckets=[]):
    if len(buckets) > 0:
        for bucket in buckets:
            template.add_resource(s3.Bucket(
                Bucket=bucket
            ))
    return TemplateGenerator(template).to_json()
    pass