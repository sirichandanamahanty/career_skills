import { RoleBenchmark, RoadmapMilestone } from '../types/career';

/**
 * Calculates the dynamic Job Readiness Score (0 - 100%)
 * based on verified initial levels and completed roadmap milestones.
 */
export function calculateJobReadiness(
  benchmark: RoleBenchmark,
  milestones: RoadmapMilestone[],
  baseScore: number = 32
): number {
  let totalTasks = 0;
  let completedTasks = 0;

  milestones.forEach(m => {
    m.tasks.forEach(t => {
      totalTasks++;
      if (t.done) completedTasks++;
    });
  });

  if (totalTasks === 0) return baseScore;

  const progressFraction = completedTasks / totalTasks;
  const targetThreshold = benchmark.benchmarkScore;
  const score = Math.round(baseScore + progressFraction * (targetThreshold - baseScore + 12));

  return Math.min(100, Math.max(0, score));
}

/**
 * Evaluates skill deficits between target requirements and current user proficiency.
 */
export function computeSkillDeficits(
  competencyLabels: string[],
  requiredLevels: number[],
  currentLevels: number[]
) {
  return competencyLabels.map((skill, index) => {
    const required = requiredLevels[index] || 0;
    const current = currentLevels[index] || 0;
    const delta = Math.max(0, required - current);

    return {
      skill,
      required,
      current,
      delta,
      isSatisfied: delta === 0
    };
  });
}
