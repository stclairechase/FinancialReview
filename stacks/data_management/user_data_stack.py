from constructs import Construct 
from aws_cdk import (
    Stack,
    RemovalPolicy,
    Attribut
)
from aws_cdk.aws_s3 import (
    Bucket,
    BucketEncryption
)
from aws_cdk.aws_kms import (
    Key, 
    Alias, 
)
from aws_cdk.aws_dynamodb import ( 
    Table,
    AttributeType, 
    Attribute
)

class UserDataStack(Stack): 

    def __init__(self, scope: Construct | None = None, id: str | None = None) -> None:
        super().__init__(scope, id)

        customer_key = Key(scope, 'financial-audit-user-data-key')
        customer_alias = Alias(scope, 'financial-audit-user-data-alias', target_key=customer_key)

        user_data_partition = Attribute(name='birthdate', type=AttributeType.STRING)
        user_data_db = Table(scope, id = 'financial-audit-user-details', partition_key=user_data_partition, encryption_key=customer_alias)

        
