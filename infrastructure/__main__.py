# Import shared resources
import pulumi
from shared.vpc import vpc
from shared.s3 import bucket
from shared.appflow import flow


# Import each lambda module
from appsync_consumer.lambda_function import lambda_function as appsync_consumer_lambda
from request_consumer.lambda_function import lambda_function as request_consumer_lambda
from zendesk_cleaner.lambda_function import lambda_function as zendesk_cleaner_lambda

project_name = pulumi.get_project()
stack_name = pulumi.get_stack()

# Rename Lambda functions according to convention
appsync_consumer_lambda.name = f"{project_name}_appsync-consumer_{stack_name}"
request_consumer_lambda.name = f"{project_name}_request-consumer_{stack_name}"
zendesk_cleaner_lambda.name = f"{project_name}_zendesk-cleaner_{stack_name}"
