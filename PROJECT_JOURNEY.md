# 🚀 Full DevOps Project History: Terraform + AWS + Git
**User:** Arun Kumar | **Location:** Guadalajara, Mexico | **Date:** March 2026

This file contains every command used to build, troubleshoot, and document my first Cloud Infrastructure project.

---

## 🏗 Phase 1: Local Environment Setup
*Setting up the workspace on my MacBook Air.*

```bash
cd ~/Desktop                 # Go to Desktop
mkdir devops_projects        # Create main project folder
cd devops_projects           # Enter the folder
terraform -version           # Check current Terraform version (v1.14.5)
brew install awscli          # Installed AWS Command Line Interface


Phase 2: AWS Cloud Integration
Linking the MacBook to the AWS Account (961883620237).

aws --version                # Verify CLI is installed
aws configure                # Input Access Key & Secret Key
# Settings used: region=us-east-1, format=json

aws sts get-caller-identity  # The "Identity Check" to confirm AWS connection


Phase 3: Terraform Deployment
Creating the S3 Bucket using Infrastructure as Code (main.tf).

touch main.tf                # Created the blueprint file
# (Added AWS provider and aws_s3_bucket resource in VS Code)

terraform init               # Downloaded the 750MB AWS Provider drivers
terraform plan               # Previewed the infrastructure (1 to add)
terraform apply              # DEPLOYED: Created the bucket in AWS
# Typed 'yes' to confirm


Phase 4: Git Troubleshooting (The Large File Fix)
GitHub rejected the upload because of the 750MB .terraform folder. Here is the fix:

touch .gitignore             # Created the filter file
echo ".terraform/" >> .gitignore  # Ignore heavy drivers
echo "*.tfstate*" >> .gitignore   # Ignore sensitive state files
echo ".terraform.lock.hcl" >> .gitignore

# The "Deep Clean" to wipe the large file from Git history:
rm -rf .git                  # Deleted the local Git record
git init                     # Restarted a fresh Git record
git remote add origin [https://github.com/arunkumarm-tech/devops_projects.git](https://github.com/arunkumarm-tech/devops_projects.git)
git add .                    # Added only the light code files
git commit -m "Fresh start with .gitignore"
git push -f origin main      # Forced a clean upload to GitHub


Phase 5: Documentation & Final Push
Finalizing the project for my LinkedIn/GitHub profile.

touch README.md              # Created the project landing page
git add README.md PROJECT_JOURNEY.md
git commit -m "Added complete project history and journey"
git push

