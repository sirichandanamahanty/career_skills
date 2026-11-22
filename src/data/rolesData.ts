import { RoleBenchmark } from '../types/career';

export const ROLES_DATABASE: Record<string, RoleBenchmark> = {
  sde: {
    title: "Software Engineer (SDE)",
    benchmarkScore: 80,
    competencyLabels: ["Prog Fundamentals", "DSA & Algorithms", "Databases / SQL", "System Architecture", "Backend APIs", "Git & DevOps"],
    benchmarkLevels: [5, 4.5, 4, 3.5, 4, 3.5],
    initialUserLevels: [3.5, 2.0, 2.5, 1.2, 1.5, 3.0],
    gaps: [
      { skill: "Data Structures & Algorithms", priority: "High", deficit: "Needs Trees, Graphs & Dynamic Programming", icon: "binary" },
      { skill: "Backend API Engineering", priority: "High", deficit: "REST, Middleware, HTTP Spec & Error Handling", icon: "server" },
      { skill: "Advanced Databases", priority: "Medium", deficit: "Indexing, Transactions (ACID) & Schema Normalization", icon: "database" },
      { skill: "System Design Basics", priority: "Medium", deficit: "Caching, Load Balancing & Horizontal Scaling", icon: "cpu" }
    ],
    milestones: [
      {
        id: "m1",
        phaseName: "Step 1: Foundation",
        title: "Core Programming Fundamentals & Environment",
        status: "completed",
        badge: "Completed",
        tasks: [
          { id: "t1_1", title: "Master Python / Java OOP & Exception Handling", hours: 4, done: true, why: "Foundation for write-clean production code." },
          { id: "t1_2", title: "Intermediate Git Workflow (Rebase, Branches, PRs)", hours: 3, done: true, why: "Standard collaboration protocol in all engineering teams." }
        ]
      },
      {
        id: "m2",
        phaseName: "Step 2: DSA Sprint",
        title: "Data Structures & Placement Problem Solving",
        status: "in-progress",
        badge: "In Progress",
        tasks: [
          { id: "t2_1", title: "Master HashMaps, Two-Pointer & Sliding Window", hours: 5, done: false, why: "Appears in 78% of initial SDE screening rounds." },
          { id: "t2_2", title: "Binary Trees, BSTs & Graph Traversals (BFS/DFS)", hours: 8, done: false, why: "Core interview staple for product-based companies." },
          { id: "t2_3", title: "Complete LeetCode 75 Curated Study Plan", hours: 15, done: false, why: "Builds problem recognition under time constraints." }
        ]
      },
      {
        id: "m3",
        phaseName: "Step 3: Backend & Databases",
        title: "Production Backend & Relational Data Modeling",
        status: "upcoming",
        badge: "Upcoming",
        tasks: [
          { id: "t3_1", title: "Build RESTful APIs with FastAPI or Express.js", hours: 6, done: false, why: "Demonstrates practical full-cycle service delivery." },
          { id: "t3_2", title: "Database Indexing, Joins & Query Optimization", hours: 5, done: false, why: "Backend engineers must understand query cost and latency." },
          { id: "t3_3", title: "Implement JWT Authentication & RBAC Middleware", hours: 4, done: false, why: "Essential security standard for real-world products." }
        ]
      },
      {
        id: "m4",
        phaseName: "Step 4: Real-World Projects",
        title: "Capstone Engineering Projects",
        status: "upcoming",
        badge: "Upcoming",
        tasks: [
          { id: "t4_1", title: "Build Scalable E-Commerce API with Redis Caching", hours: 14, done: false, why: "Shows you can build beyond basic CRUD tutorials." },
          { id: "t4_2", title: "Write Automated Unit/Integration Tests & Dockerfile", hours: 5, done: false, why: "Proves enterprise-ready deployment maturity." }
        ]
      },
      {
        id: "m5",
        phaseName: "Step 5: Resume & ATS Optimization",
        title: "Technical Resume & Portfolio Polish",
        status: "upcoming",
        badge: "Upcoming",
        tasks: [
          { id: "t5_1", title: "Format Resume using XYZ Impact Bullet Formula", hours: 3, done: false, why: "Increases ATS pass rate by 3.2x." },
          { id: "t5_2", title: "Polish GitHub READMEs with Architecture Diagrams", hours: 2, done: false, why: "First thing recruiters inspect when reviewing portfolios." }
        ]
      },
      {
        id: "m6",
        phaseName: "Step 6: Interview Drills",
        title: "Mock Technical & Behavioral Interview Drills",
        status: "upcoming",
        badge: "Upcoming",
        tasks: [
          { id: "t6_1", title: "Practice 5 Live Mock Technical Coding Rounds", hours: 6, done: false, why: "Reduces interview anxiety and trains out-loud communication." },
          { id: "t6_2", title: "Prepare STAR stories for Behavioral / Core Values", hours: 3, done: false, why: "Ensures passing hiring manager and bar-raiser rounds." }
        ]
      }
    ],
    projects: [
      {
        title: "Distributed Task Queue & Notification Engine",
        tag: "Plugs Backend & Async Gaps",
        difficulty: "Intermediate",
        tech: ["Python / Node", "Redis", "PostgreSQL", "Docker"],
        description: "A robust worker pool that processes delayed emails and webhooks with exponential backoff and retry guarantees."
      },
      {
        title: "Real-Time Collaborative Code Editor",
        tag: "Plugs System Design & WebSocket Gaps",
        difficulty: "Advanced",
        tech: ["WebSockets", "CRDTs / Operational Transforms", "Node.js"],
        description: "Multi-user synced editor demonstrating low-latency communication and conflict resolution algorithms."
      }
    ],
    certs: [
      {
        name: "AWS Certified Cloud Practitioner or Developer Associate",
        issuer: "Amazon Web Services",
        impact: "High Industry Weight",
        desc: "Validates cloud fundamentals, serverless computing, and enterprise infrastructure basics."
      }
    ]
  }
};
