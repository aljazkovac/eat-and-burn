# TODO

## GitHub account

- [x] Make `from-nand-to-tetris` and `dlai-short-courses` private and archived (the course asks students not to publish solutions)
- [x] Prepare and execute a plan for what repos to archive, make private, leave public, etc., and apply topics and descriptions across all repos
- [x] Create `playground` repo for small AI experiments (private)
- [x] Create profile repo `aljazkovac/aljazkovac` with a short README linking to the blog and current projects
  - [x] Auto-update a "Latest posts" list from the blog's `/feed.xml` with a GitHub Action
- [x] Clean up local repo clones (`~/Developer/repos`, `~/Developer/courses`, `~/Developer/archive`)
- [ ] Delete unused repos (`part2-notes`, `jekyll-tutorial`, `ai-readiness-saas`, `dlai-short-courses`)
- [ ] Pin the best 6 repos (manual, on `https://github.com/aljazkovac`):
  1. `eat-and-burn`
  2. `calorie-balance` (or `github-as-code` once created)
  3. `aljazkovac.github.io`
  4. `devops-with-kubernetes`
  5. `yarp-microservices`
  6. `SBERT-Automatic-Classification-Menu-Items`
- [ ] Create Terraform repo (`github-as-code`) for GitHub repos, and spin up/import repos with it; use GitHub Actions / Terragrunt to apply when merging a PR. Consider optimal settings (branch ruleset[...]
  - [ ] Import existing repos and manage descriptions, topics, visibility, and archiving through Terraform
- [x] Decide what to do with `_unpublished_posts/` in `aljazkovac.github.io` (moved drafts to private `aljazkovac/cockpit` repo under `writing/drafts/`)

## eat-and-burn

- [ ] Decide whether and when to merge `calorie-balance` into this repo (`backend/` + `android/` + `mcp/` + `infra/`)
- [ ] Add `CLAUDE.md` (run `/init`), `.env.example`, and `ruff` + `pytest` so agents have a feedback loop
- [ ] Create a service that pulls health data on a nightly basis and displays it in dashboards (backend, frontend)
- [ ] Create PR review agents with Copilot in GitHub, and explore other agents you can set up there
- [ ] Create an MCP wrapper to query and display this data
- [ ] Write tests for the backend, frontend and the MCP: unit, integration, E2E -> use specs and Playwright agents
- [ ] Create documentation and use a documentation tool to display it somewhere
- [ ] Host everything in the cloud, using Kubernetes and ArgoCD and Terraform with Terragrunt
- [ ] Set up observability using Prometheus and Grafana
