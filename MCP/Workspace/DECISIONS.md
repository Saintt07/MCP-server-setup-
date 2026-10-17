## Purpose: Record consequential choices so future sessions do not silently reverse them. Keep existing records; supersede a decision with a new entry that links to the earlier ID.

# Decision rules
- Log decisions affecting runtime/SDK, transport, schemas, tools, filesystem safety, auth, deployment, concurrency, or demo scope.
- State the context and alternatives considered. Explain why the chosen option fits the requirements.
- Record tradeoffs and how the decision will be validated.
- Do not record a proposal as an adopted decision. Use PROPOSED until the project owner confirms it.
- Never put tokens, passwords, private URLs containing credentials, or other secrets in this file.

# Decision record template
DEC-YYYYMMDD-01 — [short title]
- Status: PROPOSED / ACCEPTED / REJECTED / SUPERSEDED
- Date / owner: [date] / [person or session]
- Context: [problem or requirement]
- Decision: [specific choice]
- Alternatives considered:
  - [option A — benefit/cost]
  - [option B — benefit/cost]
- Rationale: [why this choice best fits this project]
- Consequences / tradeoffs: [what gets easier/harder; risks introduced]
- Security / concurrency impact: [impact or none, with explanation]
- Validation plan: [test, benchmark, client check, or review]
- Evidence / related files: [paths, commit, transcript]
- Supersedes / superseded by: [decision ID or NONE]