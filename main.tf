provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "arun_test_bucket" {
  bucket = "arun-terraform-practice-2026" 
}