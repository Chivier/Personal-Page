# Personal Homepage

Static personal academic homepage with bilingual support (English/Chinese), built with a Python generator and Jinja2 templates.

## Architecture

- `generator.py` — Main build script. Reads markdown content, compiles templates, compiles CVs via xelatex, outputs to `dist/`.
- `templates/` — Jinja2 HTML templates + CSS/JS.
- `content/` — Markdown source files with YAML frontmatter.
  - `content/authors/admin/_index.md` — Author bio (English). `_index.zh.md` for Chinese.
  - `content/publication/<slug>/index.md` — One directory per publication.
  - `content/project/<slug>/index.md` — One directory per project.
- `i18n/en.yml`, `i18n/zh.yml` — UI translation strings.
- `CV-Overleaf/` — LaTeX CV source (git subtree from `Chivier/CV-Overleaf`). Contains:
  - `main.tex` — English CV
  - `main_zh.tex` — Chinese CV
  - Both compiled with xelatex (uses `ctex` package, do NOT use `[pdftex]` option for hyperref).
- `dist/` — Generated output (gitignored). English at root, Chinese at `dist/zh/`.
- `deploy.sh` — Local build + deploy script. Pushes `dist/` to `gh-pages` branch.

## Build & Deploy

```bash
# Install Python deps
pip install -r requirements.txt

# Generate site locally (also compiles CV if xelatex is available)
python generator.py

# Build and deploy to gh-pages branch
./deploy.sh
```

## CV Subtree

CV-Overleaf is managed as a git subtree (not submodule):
```bash
# Pull upstream changes
git subtree pull --prefix=CV-Overleaf https://github.com/Chivier/CV-Overleaf.git main --squash

# Push local CV changes upstream
git subtree push --prefix=CV-Overleaf https://github.com/Chivier/CV-Overleaf.git main
```

## CI/CD

GitHub Actions (`.github/workflows/deploy.yml`) simply deploys the `gh-pages` branch to GitHub Pages. No build happens in CI — all builds are done locally via `deploy.sh`.

GitHub Pages settings: deploy from `gh-pages` branch.

## Adding Content

### New publication
Create `content/publication/<slug>/index.md` with frontmatter:
```yaml
---
title: "Paper Title"
authors: ["Author One", "Author Two"]
date: "2026-01-01T00:00:00Z"
publication: "Conference Name"
publication_short: "CONF'26"
url_pdf: ""
---
```

### New project
Create `content/project/<slug>/index.md` with similar frontmatter. Add `featured.png` for the card image.

## Key Conventions

- All templates use `{{ t.section.key }}` for translated UI strings.
- Publication/project entries are sorted by `date` descending.
- The CV social link points to `uploads/resume.pdf` (relative path).
- English CV → `dist/uploads/resume.pdf`, Chinese CV → `dist/zh/uploads/resume.pdf`.
- Keep CV content, homepage publications, and education info consistent across all three sources.

## Hydra Sub-Agent Tool

Classify the task before choosing a mode. Hydra is for file-driven
orchestration, not the default path for every change.
Hydra treats `result.json` + `done` as the only completion evidence.
Terminal conversation is not a source of truth.

Core rules:
- Root cause first. Fix the implementation problem before changing tests.
- Do not hack tests, fixtures, or mocks to force a green result.
- Do not add silent fallbacks or swallowed errors.
- A handoff is only complete when both `result.json` and `done` exist and pass schema validation.

Workflow patterns:
1. Do the task directly when it is simple, local, or clearly faster without workflow overhead.
2. Use a single implementer workflow when you still want Hydra evidence and retry control:
   `hydra run --task "<specific task>" --repo . --template single-step [--worktree .]`
3. Use the default planner -> implementer -> evaluator workflow for ambiguous, risky, or PRD-driven work:
   `hydra run --task "<specific task>" --repo . [--worktree .]`
   - If the user says all roles should use one provider, pass `--all-type <provider>`.
   - If the user wants a mix, pass `--planner-type`, `--implementer-type`, and `--evaluator-type`.
   - If the user does not specify providers, Hydra should prefer the current terminal's provider when available.
4. Use a direct isolated worker primitive when the split is already known and you do not need a full workflow:
   `hydra spawn --task "<specific task>" --repo . [--worktree .]`

Agent launch rule:
- When dispatching Claude/Codex through TermCanvas CLI, start a fresh agent terminal with `termcanvas terminal create --prompt "..."`
- Do not use `termcanvas terminal input` for task dispatch; it is not a supported automation path

Workflow control:
- After `hydra run` or `hydra spawn`, immediately start polling with `hydra watch`. Do not ask whether to watch — always watch.
1. Inspect one-shot progress: `hydra tick --repo . --workflow <workflowId>`
2. Watch until terminal state: `hydra watch --repo . --workflow <workflowId>`
3. Inspect structured state and failures: `hydra status --repo . --workflow <workflowId>`
4. Retry a failed/timed-out workflow when allowed: `hydra retry --repo . --workflow <workflowId>`
5. Clean up runtime state or worktrees: `hydra cleanup --workflow <workflowId> --repo .`

Telemetry polling:
1. Treat `hydra watch` as the main-brain polling loop; do not infer progress from terminal prose alone.
2. Before deciding wait / retry / takeover, query:
   - `termcanvas telemetry get --workflow <workflowId> --repo .`
   - `termcanvas telemetry get --terminal <terminalId>`
   - `termcanvas telemetry events --terminal <terminalId> --limit 20`
3. Keep waiting when telemetry shows recent meaningful progress, `thinking`, `tool_running`, `tool_pending`, or a foreground tool.
4. Treat `awaiting_contract` as "turn complete, file contract still pending".
5. Treat `stall_candidate` as "investigate before retry", not automatic failure.
6. Treat `error` as "agent hit an API error". Check `last_hook_error`: `rate_limit`/`server_error` → wait and retry; `billing_error`/`authentication_failed` → stop; `max_output_tokens` → retry with compact; `invalid_request` → stop and investigate.

Worker control:
1. List direct workers: `hydra list --repo .`
2. Clean up a direct worker: `hydra cleanup <agentId>`

`result.json` must contain:
- `success`
- `summary`
- `outputs[]`
- `evidence[]`
- `next_action`

When NOT to use: simple fixes, high-certainty tasks, or work that is faster to do directly in the current agent.
