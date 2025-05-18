# Project Overview

## Deployment
- **`vercel.json`**: Used to deploy both the frontend and backend.

## Backend
- Located at `./api/backend.py`.
- Built using **FastAPI**.

## Frontend
- Located at `./frontend/index.html`.
- Built using simple HTML without much hardcoding.

## Environment Variables
- `.env` file contains the secret key token provided by our professor.

## Dependencies
- **`requirements.txt`**: Contains all the dependencies required to run this project.
  - Created using the command: `pipreqs . --force`, which includes only the required dependencies.