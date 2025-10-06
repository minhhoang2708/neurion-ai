import json
import pulumi
import pulumi_aws as aws

config = pulumi.Config()
project_name = pulumi.get_project()
stack_name = pulumi.get_stack()

# This role grants the Lambda function permissions to run and write logs.
lambda_role = aws.iam.Role(
    f"neurion-ai-{project_name}-lambda-role-{stack_name}",
    assume_role_policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {"Service": "lambda.amazonaws.com"},
                }
            ],
        }
    ),
    description="IAM role for the Lambda function",
)

# Attach the basic AWSLambdaVPCAccessExecutionRole policy to the role.
# This policy allows the function to write logs to CloudWatch.
aws.iam.RolePolicyAttachment(
    f"neurion-ai-{project_name}-lambda-policy-{stack_name}",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
)

# The code for the function is an asset that points to the zip file.
lambda_function = aws.lambda_.Function(
    f"neurion-ai-{project_name}-lambda-{stack_name}",
    # The handler value is `filename.function_name`.
    handler="main.handler",
    runtime="python3.13",
    role=lambda_role.arn,
    code=pulumi.FileArchive("../../zendesk_cleaner.zip"),
    description="A simple Python Lambda function deployed with Pulumi.",
    tags={
        "project": f"neurion-ai-{project_name}-lambda",
        "stack": stack_name,
    },
)

pulumi.export("lambda_function_name", lambda_function.name)
pulumi.export("lambda_function_arn", lambda_function.arn)
