import pulumi_aws as aws

# Example S3 bucket resource
bucket = aws.s3.Bucket(
    "mainBucket",
    acl="private",
    tags={"Name": "main-bucket"}
)
