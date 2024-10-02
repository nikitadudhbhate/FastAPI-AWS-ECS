# Deploy a Python FastAPI App to AWS ECS using GitHub Actions

This project demonstrates how to containerize a Python FastAPI app and deploy it to Amazon Elastic Container Service (ECS) using GitHub Actions. The deployment uses AWS Fargate to run the Docker container.

## Prerequisites

Before starting, ensure you have the following:

- **AWS Account**: An AWS account with necessary permissions.
- **AWS CLI**: Installed and configured with access to ECS, ECR, and IAM.
- **GitHub Repository**: A repository for your FastAPI app.
- **GitHub Secrets**: Set the following secrets in your GitHub repository:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `AWS_ECR_REPOSITORY`
  - `AWS_ECS_CLUSTER`
  - `AWS_ECS_SERVICE`
  - `AWS_ECS_TASK_DEFINITION`
  - `DOCKERHUB_USERNAME` (optional, if you’re using Docker Hub)
  - `DOCKERHUB_ACCESS_TOKEN` (optional)


## Step-by-Step Deployment Guide

### Step 1: Write a FastAPI App
### Step 2: Create a Dockerfile
### Step 3: Push the Docker Image to AWS Elastic Container Registry (ECR)
- Create an ECR Repository: In your AWS account, create an ECR repository where the Docker image will be stored.
- Build and Push the Image: Use GitHub Actions to automate the process of building and pushing the image to ECR.
### Step 3: Push the Docker Image to AWS Elastic Container Registry (ECR)
- Create an ECR Repository: In your AWS account, create an ECR repository where the Docker image will be stored.

- Build and Push the Image: Use GitHub Actions to automate the process of building and pushing the image to ECR.

### Step 4: Create an ECS Task Definition
- ECS Task Definition: In AWS, create a task definition that points to your ECR repository and defines how to run the container.
- ECS Cluster: Make sure you have an ECS cluster running.
- ECS Service: Create an ECS service that will manage running the task definition on AWS Fargate.

### Step 5: Automate Deployment with GitHub Actions
- In the .github/workflows/deploy.yml file, configure GitHub Actions to build, push the Docker image to ECR, and deploy it to ECS using AWS Fargate.

### Step 6: Verify Deployment
- ECS Console: Navigate to the ECS console in AWS and confirm that your service is running.
- Access the Application: Once the task is running, access the application via the load balancer or public IP address provided by AWS.

### Conclusion
You have successfully automated the deployment of a Dockerized Python FastAPI app to AWS ECS using GitHub Actions and AWS Fargate.
