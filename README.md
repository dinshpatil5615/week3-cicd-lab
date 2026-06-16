# Week 3: CI/CD Pipeline — GitHub Actions + ECR + ECS

## What I Built
Full CI/CD pipeline — every git push automatically builds a Docker image,
pushes to AWS ECR, and deploys to ECS Fargate. Zero manual AWS steps.

## Architecture
Code → git push → GitHub Actions → Docker build → ECR push → ECS Fargate deploy

## Pipeline Steps
- Trigger: push to main branch
- Build: Docker image tagged with git commit SHA
- Push: image to AWS ECR private registry  
- Deploy: ECS service updated with zero downtime rolling update
- Validate: pipeline waits for ECS service stability before marking success

## Push-based CI/CD vs GitOps
This pipeline is PUSH-based — GitHub Actions pushes to ECS.
In GitOps (ArgoCD/Flux) the cluster PULLS changes from Git itself.
Pull-based is more secure and auto-detects configuration drift.

## Tech Stack
- GitHub Actions (CI/CD)
- AWS ECR (container registry)
- AWS ECS Fargate (serverless containers)
- Python Flask (sample app)
- Docker

## Cost
Total lab cost: under Rs 20
All resources deleted after lab with AWS CLI

git add .
git commit -m "docs: add README for Week 3 CI/CD lab"
git push origin main
