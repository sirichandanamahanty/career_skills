# Career Skill Gap AI — Backend

Universal Career Intelligence & Roadmap Engine supporting 85+ global and Indian careers across technology, business, public administration, law, healthcare, creative arts, and trades.

## 🚀 Quickstart

1. **Install Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **(Optional) Configure Gemini API Key:**
   ```bash
   # Windows PowerShell
   $env:GEMINI_API_KEY="your-gemini-api-key"

   # Linux / macOS
   export GEMINI_API_KEY="your-gemini-api-key"
   ```

3. **Run Server:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   Open API documentation at: **`http://127.0.0.1:8000/docs`**

## 📡 API Endpoints

- `GET /api/fields`: List all 10 fields of study & starting advantage text
- `GET /api/roles`: List 85+ roles with search, sector (P/V), and region (I/A) filters
- `GET /api/roles/{id}`: Full role taxonomy, skills, hours, projects, and certifications
- `POST /api/assess`: Weighted readiness calculation and sequential week-by-week roadmap
- `POST /api/ai/custom-role`: Dynamic AI generator for unlisted professions
- `POST /api/ai/ask-mentor`: AI career counselor guidance tailored to specific skill deficits
- `POST /api/progress/save`: Cloud persistence for student milestone check-offs
