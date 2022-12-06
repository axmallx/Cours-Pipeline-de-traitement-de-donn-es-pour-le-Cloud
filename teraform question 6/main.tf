resource "aws_instance" "ec2_vm" {
  ami           = "ami-02384a901b5df8024"
  instance_type = "t3.micro"
  key_name      = "mykey"
  tags = {
    Name = "amal.mimouni@etu.u-pec.fr"
    Owner = "amalmi"
  }
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
}

# Default ec2 user is "ec2-user"


variable "stream_name" {
        type = string
}

variable "partition_count" {
  type = number
  default = 1
}


resource "aws_kinesis_stream" "amal-mimouni-stock-input-stream" {
  name           = var.stream_name
  shard_count    = var.partition_count
  tags = {
        Name = "amal.mimouni@etu.u-pec.fr"
        Owner = "amalmi"
  }
}