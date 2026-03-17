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
