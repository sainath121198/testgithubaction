# testgithubaction

## CI/CD Workflow

This repository uses a pull-request based workflow: developers push feature branches (for example `sainath` branch), open a Pull Request, and the CI pipeline plus code review run before merging to `main` (production branch).

- CI: build, unit tests, lint, and SAST (CodeQL).
- Code review: approvals and security checks required before merge.

See the GitHub Actions workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml)

### Workflow Diagram

```mermaid
flowchart LR
	Dev[Developer] --> Sainath[sainath branch]
	Sainath --> PR[Pull Request / Merge Request]
	PR --> CI[CI Pipeline]
	PR --> CR[Code Review]
	CI -->|build, tests, lint, SAST| PASS{PASS?}
	CR -->|approval & review| PASS
	PASS -->|yes| Merge[Merge allowed]
	PASS -->|no| Block[Block / Fix required]
	Merge --> Main[main (Production branch)]
	Main --> CD[CD / Deployment]
	CD --> Prod[Production]

	style Dev fill:#f9f,stroke:#333,stroke-width:1px
	style Prod fill:#afa,stroke:#333,stroke-width:1px
```

