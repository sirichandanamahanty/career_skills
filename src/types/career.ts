export type PriorityLevel = 'High' | 'Medium' | 'Low';
export type MilestoneStatus = 'completed' | 'in-progress' | 'upcoming';

export interface TaskItem {
  id: string;
  title: string;
  hours: number;
  done: boolean;
  why: string;
  resourceLink?: string;
}

export interface RoadmapMilestone {
  id: string;
  phaseName: string;
  title: string;
  status: MilestoneStatus;
  badge: string;
  tasks: TaskItem[];
}

export interface SkillGap {
  skill: string;
  priority: PriorityLevel;
  deficit: string;
  icon: string;
}

export interface RecommendedProject {
  title: string;
  tag: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  tech: string[];
  description: string;
}

export interface RecommendedCertification {
  name: string;
  issuer: string;
  impact: string;
  desc: string;
}

export interface RoleBenchmark {
  title: string;
  benchmarkScore: number;
  competencyLabels: string[];
  benchmarkLevels: number[];
  initialUserLevels: number[];
  gaps: SkillGap[];
  milestones: RoadmapMilestone[];
  projects: RecommendedProject[];
  certs: RecommendedCertification[];
}

export interface StudentProfile {
  name: string;
  academic: string;
  hoursPerWeek: number;
  targetRoleKey: string;
  skills: string[];
  projectsCompleted?: string;
}
