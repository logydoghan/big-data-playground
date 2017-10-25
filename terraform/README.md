# Terraform

## AWS
For using Terraform, you need an AWS key/secret
`http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey`

With AWS access key and access key secret, change `~/.aws/credentials`:
```ini
[default]
aws_access_key_id = [你的 access key id]
aws_secret_access_key = [你的 access key secret]
```

Access ec2 from remote ssh, you need an ec2 keypair
`http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html`

After getting AWS EC2 private key, save it locally。Run this to grant private key permission
```sh
chmod 400 [private key的位置]
```
