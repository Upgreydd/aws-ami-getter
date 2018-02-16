
# AWS AMI Getter
Script will download Latest Amazon Linux AMI hash for latest image from https://aws.amazon.com/amazon-linux-ami/ site.

### AVAILABLE REGIONS:
- US East N. Virginia (us-east-1)
- US East Ohio (us-east-2)
- US West Oregon (us-west-2)
- US West N. California (us-west-1)
- Canada Central (ca-central-1)
- EU Ireland (eu-west-1)
- EU London (eu-west-2)
- EU Paris (eu-west-3)
- EU Frankfurt (eu-central-1)
- Asia Pacific Singapore (ap-southeast-1)
- Asia Pacific Seoul (ap-northeast-2)
- Asia Pacific Tokyo (ap-northeast-1)
- Asia Pacific Sydney (ap-southeast-2)
- Asia Pacific Mumbai (ap-south-1)
- South America São Paulo (africa)
- China Beijing (china)
- AWS GovCloud (gov)

### AVAILABLE AMI TYPES:
- HVM (SSD) EBS-Backed 64-bit (hvm-ebs)
- HVM Instance Store 64-bit (hvm-is)
- PV EBS-Backed 64-bit (pv-ebs)
- PV Instance Store 64-bit (pv-is)
- HVM (NAT) EBS-Backed 64-bit (hvm-ebs-nat)
- HVM (Graphics) EBS-Backed 64-bit (hvm-ebs-gfx)

### USAGE:
./main.py region ami-type

### EXAMPLE:
./main.py ap-south-1 hvm-ebs
