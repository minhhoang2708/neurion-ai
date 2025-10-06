import pulumi_aws as aws
import pulumi

project_name = pulumi.get_project()

# Basic Lambda execution role with logging
lambda_role = aws.iam.Role(
    f"{project_name}_appsyncConsumerLambdaRole",
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
    f"{project_name}_appsyncConsumerLambdaBasicExecution",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

lambda_function = aws.lambda_.Function(
    "appsyncConsumerLambda",
    runtime="python3.13",
    code=pulumi.FileAsset("../../appsync_consumer.zip"),
    handler="main.handler",
    role=lambda_role.arn,
    timeout=300,
    memory_size=256,
)
