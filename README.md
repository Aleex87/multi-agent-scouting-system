# multi-agent-scouting-system

## Project Overview

This project implements a **multi-agent workflow for sports scouting**, designed to analyze a team and suggest potential player replacements or improvements.

The system is **dynamic and sport-agnostic**, meaning it can be applied to different sports, not only football. The goal is not to build a fully accurate scouting system, but to demonstrate how a **multi-agent architecture** can be translated into working code using a structured workflow.

The implementation focuses on:
- Clear agent responsibilities
- Structured communication between agents
- Logging and traceability
- Human-in-the-loop decision making
- Safe and controlled execution (guardrails)

---

## Core Architecture: Planner – Doer – Critic

The system follows the **Planner–Doer–Critic pattern**, where each agent has a clearly defined role:

- **Planner** → analyzes the team and identifies needs  
- **Doer** → finds a potential player candidate  
- **Critic** → validates the candidate  
- **Human-in-the-Loop** → makes the final decision  

This separation of concerns improves:
- Quality
- Traceability
- Reliability

---

## Workflow Description

### 1. Input

The scout provides:
- A team (their own or another team)
- Players, positions, and basic performance data

---

### 2. Agent 1 – Planner (Analyze Team)

The Planner analyzes the team and identifies weaknesses.

Responsibilities:
- Detect missing positions (empty roles)
- Identify underperforming players (low score)

Output:
- Target position or player to replace
- Requirements for the replacement (role, performance criteria)

This output acts as a structured brief for the next agent.

---

### 3. Agent 2 – Doer (Find Player)

The Doer receives the requirements and searches for a suitable candidate.

Responsibilities:
- Identify a player that fits the required role
- Estimate the potential value added to the team
- Optionally simulate reasoning using an LLM

Output:
- Candidate player name
- Reasoning behind the selection
- Estimated fit / value

> Note:  
> The original design includes a **private scout database** as a data source.  
> This is **not implemented in this project** to keep the system simple, but it is described in the diagram as a possible extension.

---

### 4. Agent 3 – Critic (Verification)

The Critic validates the proposed candidate.

Responsibilities:
- Verify that the player exists
- Check if the player is available (simulated market logic)
- Estimate cost or feasibility
- Evaluate if the suggestion makes sense

If the candidate is **not valid**:
- The system loops back and tries another option

If the candidate is **valid**:
- A structured recommendation is created

---

### 5. Iteration Loop (Controlled)

The system includes a loop between agents to refine results.

Purpose:
- Avoid poor suggestions
- Improve quality through iteration
- Prevent infinite or expensive processing

Constraint:
- Maximum number of iterations is limited (e.g. number of players in the team)

Each iteration is:
- Logged
- Traceable

---

### 6. Human-in-the-Loop

Before any final action, a human decision is required.

The scout can:
- Accept the suggestion
- Reject it
- Save it for later
- Take action (e.g. initiate a transfer)

The process is only considered complete after human validation.

---

## Security & Guardrails

The system includes basic safeguards inspired by real-world multi-agent risks:

### 1. Least Privilege
Each agent has limited responsibilities and access:
- No agent has full system control
- Actions are scoped and controlled

---

### 2. Controlled Data Flow
- Only necessary information is passed between agents
- Outputs are structured and minimal

---

### 3. Logging & Traceability
The system logs:
- Agent decisions
- Iteration steps
- Workflow transitions

This enables:
- Debugging
- Auditability
- Transparency

---

### 4. Loop Control
To avoid infinite loops and high costs:
- A **maximum iteration limit** is enforced

---

### 5. Human-in-the-Loop for Critical Actions
Any action with real-world impact requires:
- Explicit human approval

---

### 6. Separation of Concerns
Each agent has a single responsibility:
- Planner → analysis
- Doer → execution
- Critic → validation

This reduces:
- Errors
- Hallucinations
- Responsibility overlap

---

## Summary

This project demonstrates how a conceptual **multi-agent workflow** can be translated into code by:

- Structuring agents with clear roles
- Designing explicit input/output handoffs
- Adding logging and safety constraints
- Including human oversight

The focus is not on model accuracy, but on building a **clean, testable, and extensible multi-agent system**.