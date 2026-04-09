# Phase 7: Infrastructure as Code with Terraform

This project provisions a live AWS EC2 instance and deploys a Dockerized application using Terraform.

## Tech Stack
- **IaC:** Terraform
- **Cloud:** AWS (EC2)
- **Container:** Docker (arunmxbox/my-python-app:v1.0)

## Security Note
This project uses a .gitignore file to ensure AWS credentials are never pushed to GitHub.

# Phase 7: Infrastructure as Code with Terraform

This project provisions a live AWS EC2 instance and deploys a Dockerized application using Terraform. 

## 🚀 The Project Journey (April 8-9 Troubleshooting Log)
*Documenting the real-world engineering hurdles solved during this deployment.*

### 1. Local Orchestration & Port Mapping
Validated the Flask + Redis stack locally on macOS. 
- **Conflict:** App was unreachable at `localhost:5000`.
- **Resolution:** Identified host mapping to `5001`. Verified logic at `http://localhost:5001`.

### 2. Architecture Mismatch (ARM64 vs. AMD64)
- **Problem:** MacBook Air (Silicon) builds produced ARM64 images, causing "Exec format" errors on AWS `t2.micro` (Intel).
- **The Fix:** Utilized cross-platform builds for cloud compatibility.
- **Command:** `docker build --platform linux/amd64 -t arunmxbox/my-python-app:v1.0 .`

### 3. Terraform Triage
- **Duplicate Providers:** Resolved a state conflict by consolidating AWS provider logic into `main.tf` and purging `providers.tf`.
- **Dynamic AMI Discovery:** Replaced hardcoded IDs with a `data "aws_ami"` block to automatically fetch the latest Ubuntu 22.04 LTS image.
- **Automation:** Implemented a `user_data` script to automate Docker installation and service orchestration on boot.

### 4. SRE Audit & Cost Management
To protect my 2018 AWS account, a full decommissioning was performed after validating the live IP (`54.226.248.139`):
- **Terraform Destroy:** Automated teardown of tracked resources.
- **Manual Cleanup:** Terminated a "ghost" instance orphaned during state drift.
- **Verification:** Confirmed 0 Elastic IPs and 0 active EBS Volumes in the console.

## 🛠 Tech Stack
- **IaC:** Terraform
- **Cloud:** AWS (EC2, VPC, Security Groups)
- **Containerization:** Docker (arunmxbox/my-python-app:v1.0)
- **Backend:** Redis (Alpine)
- **Frontend:** Python (Flask)

## 🛡 Security Note
This project uses a `.gitignore` file to ensure AWS credentials and Terraform local state files are never pushed to GitHub.