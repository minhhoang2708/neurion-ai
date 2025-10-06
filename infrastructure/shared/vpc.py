import pulumi_aws as aws

# Example VPC resource
vpc = aws.ec2.Vpc(
    "mainVpc",
    cidr_block="10.0.0.0/16",
    enable_dns_support=True,
    enable_dns_hostnames=True,
    tags={"Name": "main-vpc"}
)
