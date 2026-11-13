# Grantha

AI-assisted book translation studio. Initial language priority: Sanskrit → Telugu.

## Current milestone (0.1 foundation)
- Public web dashboard with book upload and live job polling.
- Text extraction for selectable-text PDF, DOCX, EPUB and TXT.
- Page/chunk-by-chunk translation through a server-side Gemini API key.
- Per-page results and progress reporting.
- Docker-based API + web deployment foundation.

## Not implemented yet
Scanned-PDF OCR, original image/layout preservation, persistent job queue and database, user accounts, private object storage, review/edit workflow, DOCX/PDF/EPUB export, offline desktop/intranet package, and production abuse controls.

## Run locally
Requires Python 3.12+.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
# Set GEMINI_API_KEY in .env (or in your shell environment)
uvicorn backend.app:app --reload
```

Open http://127.0.0.1:8000.

## API
- `GET /api/health`
- `POST /api/jobs` multipart fields: `file`, `target_language`
- `GET /api/jobs/{job_id}`

## Important limitations
Jobs are currently held in process memory. Restarting the server loses job state and results. This is a development foundation, not a production-ready public service. Scanned PDFs currently return a clear extraction error rather than silently producing empty translations.

## Privacy and cost
Never commit API keys or book files. The server sends extracted text to the configured AI provider. Review that provider's current data-use terms before processing private or copyrighted material. API usage may incur charges; public free quotas are not an unlimited hosting plan.

## Deployment shape
GitHub stores source and runs CI/CD. The deployed API performs runtime translation. Do not use GitHub Actions as the per-page inference server.
