import pulumi_aws as aws

# Example AppFlow resource (minimal, for demo)
flow = aws.appflow.Flow(
    "exampleFlow",
    flow_name="example-flow",
    source_flow_config={
        "connector_type": "S3",
        "source_connector_properties": {
            "s3": {"bucket_name": "main-bucket"}
        }
    },
    destination_flow_config_list=[{
        "connector_type": "S3",
        "destination_connector_properties": {
            "s3": {"bucket_name": "main-bucket"}
        }
    }],
    tasks=[],
    trigger_config={"trigger_type": "OnDemand"}
)
