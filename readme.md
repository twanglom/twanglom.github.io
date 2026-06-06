# Personal Page

Fullstack personal website for Thanasak Wanglomklang, organized according to `fullstack-deploy-guide.docx`.

## Stack

| Layer | Technology | Host |
| --- | --- | --- |
| Frontend | React + Vite | Firebase Hosting |
| Backend | FastAPI | Google Cloud Run |
| Static CV | Vite public assets | Firebase Hosting |

## Project Structure

```text
frontend/                React + Vite personal website
backend/                 FastAPI portfolio API
cvfiles/                 Source CV PDF
frontend/public/         Public CV, project cover images, and downloadable files
backup/reference/        Reference demos and original source assets
```

The old static GitHub Pages HTML/CSS files have been removed from the active app. The personal page now uses `frontend/` and `backend/`.

## Local Development

Install backend dependencies:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Install and run the frontend in another terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open:

```text
http://127.0.0.1:5173
```

The homepage shows `Portfolio API connected` when the backend is running.

You can also run the frontend from the repository root:

```powershell
npm run dev
```

## Environment Files

Backend:

```text
backend/.env
```

```env
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Frontend:

```text
frontend/.env.local
```

```env
VITE_API_URL=http://127.0.0.1:8000
```

For production, set `VITE_API_URL` to the Cloud Run backend URL before `npm run build`.

## Build Checks

Frontend:

```powershell
cd frontend
npm run build
```

Backend import check:

```powershell
cd backend
python -c "from app.main import app; print(app.title, app.version)"
```

## Deploy Backend to Google Cloud Run

From the repository root:

```powershell
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
gcloud run deploy personal-page-api --source backend --region asia-northeast1 --allow-unauthenticated
```

After deployment, copy the Cloud Run service URL.

## Deploy Frontend to Firebase Hosting

From `frontend/`:

```powershell
Copy-Item .firebaserc.example .firebaserc
firebase login
firebase use YOUR_FIREBASE_PROJECT_ID
$env:VITE_API_URL="https://YOUR_CLOUD_RUN_URL"
npm run build
firebase deploy --only hosting
```

## Reference Backup Notes

- `backup/reference/RotorAI/` is the Physics-AI demo source used as page content reference.
- `backup/reference/rotor-digital-twin/` is the digital twin demo source used as page content reference.
- `backup/reference/software_images/` and `backup/reference/downloads/` keep the original restored assets.
- The active deployed copies are in `frontend/public/software_images/` and `frontend/public/downloads/`.
- Public demo URLs can be added later in `backend/app/portfolio_data.py`.
