# CareerSkillGap AI — Frontend Application

> **Tagline:** *Turn Your Skills into Your Career Roadmap.*  
> **Philosophy:** *“Instead of giving every student the same roadmap, we give every student a roadmap based on where they are and where they want to go.”*

---

## 🚀 How to Run the App Instantly (Zero Dependencies)

You can run this application immediately without installing Node.js, npm, or any build tools!

1. Open File Explorer and navigate to:
   ```
   C:\Users\DB 14 PLUS\.gemini\antigravity\scratch\career-skillgap-ai
   ```
2. Double-click **`index.html`** to open it directly in Google Chrome, Microsoft Edge, Brave, or Firefox.

Everything runs locally in your browser with interactive state management, Chart.js radar charts, dynamic Readiness Score updates, and confetti feedback.

---

## 🌟 Key Frontend Features Included

1. **Dynamic Job Readiness Gauge (SVG Engine):**
   - Calculates real-time placement readiness percentage.
   - Automatically recalibrates when you check off tasks in the roadmap.
   - Visually indicates stages: *Foundation Stage* → *Intermediate Acceleration* → *Placement Ready (80%+)*.

2. **Skill Gap Detection & Competency Radar:**
   - Visualizes your current proficiency (1-5) against market expectations for your target role.
   - Highlights high-priority deficits (e.g. Trees & Graphs in DSA, REST APIs, SQL transactions, Redis caching).

3. **Personalized Roadmap (Sequential DAG):**
   - Step 1: Foundation (Core OOP, Advanced Git)
   - Step 2: DSA Sprint (HashMaps, Two-Pointer, Trees, LeetCode 75)
   - Step 3: Backend & Databases (RESTful APIs, PostgreSQL Indexing, JWT Auth)
   - Step 4: Real-World Projects (Distributed Task Queue, E-Commerce Microservices)
   - Step 5: Resume & ATS Optimization (XYZ Impact bullet formula)
   - Step 6: Mock Technical & Behavioral Interview Drills
   - Each task includes an explicit **"Why learn this?"** rationale.

4. **Gap-Targeted Projects & Certifications:**
   - Project cards designed to directly plug identified deficits instead of generic tutorial clones.
   - Industry-recognized certification recommendations (AWS Developer, Meta Backend, DeepLearning.AI).

5. **AI Career Assistant (Interactive Simulator):**
   - Chat with an AI career mentor grounded in your profile and skill gaps.
   - Pre-loaded with realistic queries (*"Why learn SQL before MongoDB?"*, *"How to split 12 hours weekly?"*).

6. **Diagnostic Student Profile Modal:**
   - Switch target roles (*Software Engineer, Backend, Frontend/Fullstack, AI/ML, Data Engineer*).
   - Adjust available weekly hours (6, 12, or 20 hrs/week) to see timeline recalibrations.

---

## 📁 Project Structure

```
career-skillgap-ai/
├── index.html               # Self-contained, zero-dependency browser app (HTML5 + Tailwind + Chart.js)
├── README.md                # Quickstart and architecture guide
└── src/                     # Modular TypeScript/React components for Next.js / Vite projects
    ├── types/
    │   └── career.ts        # TypeScript schemas (StudentProfile, SkillGap, RoadmapMilestone, etc.)
    ├── data/
    │   └── rolesData.ts     # Benchmark role taxonomies, gaps, and milestones
    ├── utils/
    │   └── scoring.ts       # Mathematical scoring formula & delta gap calculation
    └── components/
        └── Dashboard.tsx    # Modular React component for the main dashboard view
```

---

## 💡 Using with React / Next.js / Vite

If you want to integrate this into a Next.js or Vite React application:
1. Copy the files in `src/` to your project's `src/` folder.
2. Install dependencies:
   ```bash
   npm install lucide-react chart.js react-chartjs-2 canvas-confetti
   npm install -D @types/canvas-confetti
   ```
3. Import `Dashboard` and `ROLES_DATABASE` into your page.
