
# AWS Serverless Starbucks Data Pipeline

An automated serverless data processing project using AWS services and Python to process Starbucks beverage data.

## Project Overview

This project automates CSV data processing using Amazon S3 and AWS Lambda. When a CSV file is uploaded to the input folder, an S3 event automatically triggers Lambda to process the dataset and generate a summary CSV file.

## AWS Services Used

- Amazon S3 – Stores input and processed CSV files.
- AWS Lambda – Executes Python data processing code.
- AWS IAM – Manages secure permissions.
- Amazon CloudWatch – Monitors Lambda execution logs.

## Architecture

S3 (Raw Data) → S3 Event Trigger → AWS Lambda → S3 (Processed Data)

CloudWatch monitors Lambda executions.

## Project Workflow

1. Created an S3 bucket in the Mumbai region.
2. Uploaded the Starbucks CSV dataset.
3. Created an IAM execution role for Lambda.
4. Configured permissions for S3 access and CloudWatch logging.
5. Developed a Python Lambda function using Boto3 and CSV.
6. Processed Starbucks beverage data by category.
7. Configured an automatic S3 event trigger for CSV uploads.
8. Stored the generated summary CSV in the processed-data folder.

## Input Dataset

File: starbucks.csv

Location: S3 / raw-data/

## Output

File: starbucks_category_summary.csv

Location: S3 / processed-data/

Processing result:
- 9 beverage categories
- 202 processed records represented in the summary

## Technologies

- AWS
- Python
- Boto3
- Git
- GitHub

## Key Learnings

- Serverless architecture
- S3 event notifications
- Lambda execution roles
- IAM least-privilege permissions
- Automated CSV processing
- CloudWatch monitoring

## AWS Region

Asia Pacific (Mumbai) – ap-south-1
