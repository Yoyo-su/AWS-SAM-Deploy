# create an s3 bucket
aws s3 mb s3://my-sam-bucket-ia25

# package the SAM application
aws cloudformation package --s3-bucket my-sam-bucket-ia25 --template-file template.yaml --output-template-file gen/packaged-template.yaml

# deploy the SAM application
aws cloudformation deploy --template-file gen/packaged-template.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM