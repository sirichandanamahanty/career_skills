import React from 'react';
import { RoleBenchmark, RoadmapMilestone, TaskItem } from '../types/career';

interface DashboardProps {
  roleData: RoleBenchmark;
  readinessScore: number;
  studentName: string;
  onNavigateTab: (tab: string) => void;
  onToggleTask: (milestoneId: string, taskId: string) => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  roleData,
  readinessScore,
  studentName,
  onNavigateTab,
}) => {
  const circumference = 251.2;
  const strokeOffset = circumference - (readinessScore / 100) * circumference;

  return (
    <div className="space-y-6">
      {/* Banner */}
      <div className="relative overflow-hidden rounded-2xl border border-indigo-500/30 bg-gradient-to-r from-slate-900 via-indigo-950/40 to-slate-900 p-6 shadow-xl">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="space-y-1.5">
            <span className="inline-flex items-center gap-1 text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              ● Analysis Active
            </span>
            <h1 className="text-2xl font-bold tracking-tight text-white">
              Welcome back, {studentName} 👋
            </h1>
            <p className="text-sm text-slate-300 max-w-2xl">
              Target role: <strong className="text-indigo-400">{roleData.title}</strong>. Complete the sequential milestones to bridge your key skill gaps and raise your readiness score.
            </p>
          </div>
          <button
            onClick={() => onNavigateTab('roadmap')}
            className="px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-sm font-semibold text-white transition-all shadow-lg shadow-indigo-500/25"
          >
            Continue Roadmap
          </button>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {/* Readiness Gauge */}
        <div className="rounded-2xl border border-slate-800 bg-slate-900/90 p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-slate-100">Job Readiness Score</h3>
            <span className="text-xs px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-400">Live</span>
          </div>

          <div className="my-4 flex items-center justify-center">
            <div className="relative w-36 h-36 flex items-center justify-center">
              <svg className="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="40" stroke="currentColor" strokeWidth="8" className="text-slate-800" fill="transparent" />
                <circle
                  cx="50"
                  cy="50"
                  r="40"
                  stroke="currentColor"
                  strokeWidth="8"
                  className="text-indigo-500 transition-all duration-700 ease-out"
                  fill="transparent"
                  strokeDasharray="251.2"
                  strokeDashoffset={strokeOffset}
                  strokeLinecap="round"
                />
              </svg>
              <div className="absolute flex flex-col items-center">
                <span className="text-3xl font-extrabold text-white">{readinessScore}%</span>
                <span className="text-[11px] font-semibold text-amber-400">
                  {readinessScore >= 80 ? 'Placement Ready' : 'In Progress'}
                </span>
              </div>
            </div>
          </div>

          <div className="pt-3 border-t border-slate-800 text-xs text-slate-400 flex justify-between">
            <span>Placement Threshold: 80%</span>
            <span className="text-indigo-400 cursor-pointer" onClick={() => onNavigateTab('roadmap')}>
              View Steps →
            </span>
          </div>
        </div>

        {/* Top Skill Gaps */}
        <div className="rounded-2xl border border-slate-800 bg-slate-900/90 p-5 flex flex-col justify-between">
          <h3 className="text-base font-bold text-slate-100 mb-3">Top Identified Gaps</h3>
          <div className="space-y-2">
            {roleData.gaps.map((gap, i) => (
              <div key={i} className="p-2.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs">
                <div className="flex justify-between font-semibold text-slate-200">
                  <span>{gap.skill}</span>
                  <span className="text-rose-400">{gap.priority}</span>
                </div>
                <p className="text-[11px] text-slate-400 mt-0.5">{gap.deficit}</p>
              </div>
            ))}
          </div>
          <div className="pt-3 border-t border-slate-800 text-xs text-slate-400">
            Targeting {roleData.gaps.length} critical competencies
          </div>
        </div>

        {/* What to learn next */}
        <div className="rounded-2xl border border-slate-800 bg-slate-900/90 p-5 flex flex-col justify-between">
          <div>
            <span className="text-[10px] font-bold uppercase tracking-wider text-cyan-400">Action, Not Just Advice</span>
            <h3 className="text-base font-bold text-slate-100 mt-1">What to Do Next</h3>
          </div>
          <div className="my-3 p-3.5 bg-slate-950/70 rounded-xl border border-slate-800 space-y-1.5 text-xs">
            <span className="text-indigo-400 font-bold">Phase 2: DSA Sprint</span>
            <p className="font-semibold text-slate-200">Master HashMaps & Two-Pointer Patterns</p>
            <p className="text-slate-400 text-[11px]">78% of initial coding rounds assess these exact data structure patterns.</p>
          </div>
          <button
            onClick={() => onNavigateTab('roadmap')}
            className="w-full py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-200 transition-colors"
          >
            Open Roadmap Checklist
          </button>
        </div>
      </div>
    </div>
  );
};
