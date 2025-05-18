# Project Overview

## Deployment
- **`vercel.json`**: Configuration file for deployment.
  - `./api/vercel.json`: Used for deploying the backend.
  - `./vercel.json`: Used for deploying the frontend.
- Backend entry point located at `./api/backend.py`.
- Built using **FastAPI**.

## Frontend
- Located at `./frontend/index.html`.
- Built using simple HTML with dynamic API endpoint configuration for backend integration.

## Environment Variables
- `.env` file contains the secret key token provided by our professor.
  - **Note**: Ensure the `.env` file is kept secure and is not committed to version control. Use a `.gitignore` file to exclude it from being tracked by Git.

## Dependencies
- **`requirements.txt`**: Contains all the dependencies required to run this project.
  - Created using the command: `pipreqs . --force`, which includes only the required dependencies.

## Debug Log

## Logic 0: Deploy Backend Locally Using Uvicorn and Run Frontend Locally/In Browser

### Observation
- **Frontend**:
  - **Bug 1**: Integration issue with the backend.
  - **Debug 1**: Fixed the code.
    - **Status**: Backend call failed.
    - **Conclusion**: Frontend worked as designed, but backend requests were denied.
    - **Insight**: The issue was with the design and how the backend was calling the LLM.
  - **Result**: After resolving the issue, it worked. Also applied some UI alterations.

- **Backend**:
  - Deployed locally using Uvicorn.
  - **Bug 2**: Backend requests were denied.
  - **Debug 2**: Reset API call to use OpenAPI proxy AI token.
  - **Debug 1**: Reset API call to use OpenAPI proxy AI token.
    - **Status 0**: OpenAPI call method was outdated.
    - **Status 1**: OpenAPI is a paid service.
      - **Solution 0**: Use a local LLM or Open LLM that provides API token keys.
      >- **Solution 1**: Use proxy API token keys provided by the institute.
      - **Status 3**: Deployed using Uvicorn, tested with curl, and found working.
    - **Conclusion**: OpenAPI keys could not be used in this FastAPI environment due to technical restrictions.
    - **Solution**: Used AI proxy token keys as an alternative.
    - **Insight**: OpenAPI provides API token keys for AI communication, but they cannot be used inside this FastAPI due to some technical  restrictions.  
  - **Result**: Success!

### Result
- Local backend and frontend worked successfully.

### Conclusion
- Local deployment of backend and frontend was successful.

---

## Global Deployment Using Vercel

### Logic 1: Deploy Frontend and Backend Together
This logic was attempted to simplify deployment by hosting both the frontend and backend on the same platform for seamless integration.

- **Status**: Frontend and backend were deployed, but issues arose.
  - **Bug 3**: Backend was not accessible due to network configuration issues. The backend server was not reachable because the deployment platform did not correctly route requests to the backend endpoint.
  - **Bug 1**: Backend was not accessible due to network configuration issues. The backend server was not reachable because the deployment platform did not correctly route requests to the backend endpoint.
  - **Issue 2**: Deployment logs indicated missing environment variables required for backend functionality.
  - **Isuue 3**: environment variable was uploaded but it still was not able to connect with the backend which idecate the failuer in **logic 1**.
  - **Bug 4**: Local backend was accessible!
  - **Bug 2**: Local backend was accessible!
  - **Status**: Frontend was able to fetch call from local backend.
  - **Debug**: local backend was running using **logic 0** as the depolyed frontend has a backup code which may trigger in absance of golbal backend.
  - **Conclusion**:Worded using local backend.
  - **Insight**: this logic works only when there is local backend running or it may result in failuer if local backend is not running.  
  - **Result**: partial_Success!

#### Result
- **golbal frontend** worked successfully using **local backend**.
- this indicates that deploying both frontend and backend will be tough to attain so it wolud be better to swtich to next **Logic 2**

#### Conclusion
- Golbal deployment of backend was unsuccessful.
- Golbal deployment of frontend was successful using local backend as backup.
---

### Logic 2: Deploy Frontend and Backend Separately

#### Test One
- **Objective**: Test the deployment of the frontend and backend separately to ensure they function independently and integrate correctly.
- **Steps**:
  1. Deployed the backend using Uvicorn on a cloud server.
  2. Configured the frontend to make API calls to the backend's public URL.
  3. Tested the frontend in a browser to verify API integration.
- **Observation**:
  - Backend responded correctly to API requests.
  - Frontend displayed data fetched from the backend without errors.
- **Result**: Successful deployment and integration of the frontend and backend when hosted separately.
#### Test Two
- **Objective**: Verify the robustness of separate deployment by testing with different configurations.
- **Steps**:
  1. Deployed the backend on a different cloud server with a new public URL.
  2. Updated the frontend to point to the new backend URL.
  3. Tested the frontend in multiple browsers and devices.
- **Observation**:
  - Backend responded correctly to API requests.
  - Frontend displayed data fetched from the backend without errors.
- **Result**: Successful deployment and integration under varied configurations.
- **Details**: (To be added.)
