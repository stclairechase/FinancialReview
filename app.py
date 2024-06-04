#!/usr/bin/env python3

import aws_cdk as cdk

from stacks.data_management.user_data_stack import UserDataStack
from stacks.processing.lambda_stack import LambdaStack


app = cdk.App()



LambdaStack(app, "LambdaStack")

app.synth()
