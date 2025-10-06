import pulumi_aws as aws
import pulumi

# Basic Lambda execution role with logging
lambda_role = aws.iam.Role(
    "zendeskCleanerLambdaRole",
    assume_role_policy='''{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": "sts:AssumeRole",
          "Principal": {"Service": "lambda.amazonaws.com"},
          "Effect": "Allow",
          "Sid": ""
        }
      ]
    }'''
)

aws.iam.RolePolicyAttachment(
    "zendeskCleanerLambdaBasicExecution",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

lambda_function = aws.lambda_.Function(
    "zendeskCleanerLambda",
    runtime="python3.13",
    code=pulumi.FileAsset("../../zendesk-cleaner.zip"),
    handler="main.handler",
    role=lambda_role.arn,
    timeout=300,
    memory_size=256,
)
