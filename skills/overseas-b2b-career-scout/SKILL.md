---
name: overseas-b2b-career-scout
description: Turn industry research into a concise, action-first overseas B2B sales job map centered on target companies and verified live JD links. Use when the user asks to research an industry for career entry, identify leaders/challengers/hidden champions, compare companies or sales roles, assess Europe or Singapore/Malaysia opportunities, find current overseas-sales jobs, or build a prioritized application strategy. Default to a skimmable job-search deliverable rather than a long industry lecture unless the user explicitly requests deep research.
---

# Overseas B2B Career Scout

Convert industry research into a career investment decision for overseas ToB sales. Optimize for what the user can learn, own, and carry into a stronger role after three years—not for company fame, stock performance, or headline market size.

## Default to an action-first deliverable

Treat the user's decision as the product and the research as supporting work.

- Lead with a `30 秒结论`: best industry-chain entry, most realistic first employer type, highest-value second step, and roles to avoid.
- Make target companies and verified openings the body of the report. Aim for at least 60% of useful content to be company selection, application routing, and live recruiting.
- Build a practical company pool, normally 25–40 companies when the industry supports it. Tier it into `A：每周查看并优先投`, `B：有匹配岗位再投`, and `C：补充观察`.
- For every company, show the valuable role type, target geography, reason to care, main entry barrier, and a clickable official recruiting or company entry.
- Keep industry cycle, chain mapping, scoring, and methodology concise. Do the full analysis internally, but expose only the distinctions that change where the user applies.
- Use no more than six H2 sections before `## 实时招聘结果` by default. Do not repeat the same conclusion as an industry map, ranking, career-capital section, and risk section.
- If user background is missing, give conditional routes for 0–1 years, 2–5 years, technical-to-sales, European-language/work-right holders, and Singapore work-right holders. Do not bury the result in caveats.
- Expand into a deep research report only when the user explicitly asks for detailed industry, financial, competitive, or evidence analysis.

## Apply non-negotiable geography rules

- Prioritize Europe and Singapore/Malaysia. Treat Europe as distinct country or regional markets rather than one block.
- Treat Thailand, Vietnam, and Indonesia as yellow-zone markets. Mention or recommend them only when the role is unusually strong, the strategic reason is explicit, and the territory is not a disguised broad-SEA assignment. Label the exception.
- Hard-exclude the Philippines, Cambodia, and Myanmar. Do not recommend them, count them as geographic fit, or let a broad territory title hide exposure to them.
- Verify the actual territory, customer/revenue mix, travel expectations, and location. A title such as `SEA Sales` or `APAC Sales` is not evidence of Singapore/Malaysia ownership.

Read [references/geography-and-scoring.md](references/geography-and-scoring.md) before scoring markets, companies, or roles.

## Route the request

- For an industry scan, read all reference files and use the action-first template by default.
- For a company comparison, read geography/scoring, industry/company research, ToB sales/career capital, and research methodology.
- For a JD or offer comparison, read geography/scoring, ToB sales/career capital, job-market intelligence, and output templates.
- For a live job search, read job-market intelligence, research methodology, and output templates; map enough of the industry and company context to judge role quality.

## Run the research workflow

1. **Clarify the decision.** Identify the industry, user background if known, graduate/experienced status, language or technical constraints, and intended market. Use known profile facts; do not invent missing ones. If details are absent, state one compact assumption line and give conditional routes.
2. **Research the industry internally.** Classify the cycle; map products, systems, channels/integrators, and end uses; identify what customers buy and which nodes create technical, deal, channel, and international career capital.
3. **Select only decision-changing insights.** Surface the best one to three entry nodes and the weak nodes to avoid. Do not publish a textbook-style chain walkthrough unless requested.
4. **Build the company application pool.** Identify leaders, challengers, hidden champions, distributors, integrators, and relevant local employers. Separate company strength, overseas-sales career value, and entry realism.
5. **Verify overseas fit.** Look for entities/offices, local employees, distributors, service capability, customers, certifications, exhibitions, revenue, partnerships, and hiring. Distinguish export-only, channel expansion, local operation, and mature regional business.
6. **Judge role quality.** Infer the real motion from responsibilities—not the title. Distinguish KA, solution sales, regional ownership, channel, project sales, BD, trade/quotation work, telesales, and lead generation.
7. **Search live recruiting broadly and verify deeply.** Cover every A-tier company plus relevant B-tier and local integrator searches. Follow the source, freshness, deduplication, and stopping rules in [references/job-market-intelligence.md](references/job-market-intelligence.md).
8. **Produce the action map.** Use [references/output-templates.md](references/output-templates.md). Keep evidence, inference, and unknowns distinct, but keep method out of the foreground.

Read [references/industry-company-research.md](references/industry-company-research.md) for mapping and company discovery. Read [references/tob-sales-and-career-capital.md](references/tob-sales-and-career-capital.md) for customer buying logic, role diagnosis, and career-capital tests. Read [references/research-methodology.md](references/research-methodology.md) for evidence and citation standards.

## Enforce the recruiting-table ending

For every industry report, place all live recruiting results in **one final section and one table at the absolute end of the report**.

- Do not scatter job listings through company profiles.
- Do not add summaries, caveats, sources, footnotes, or next steps after the recruiting table.
- Put referral codes, exclusive application paths, and useful school-page-only intelligence in the table's `提醒/独家信息` cell.
- Use direct, clickable job or official application links. Never fabricate a URL or label a generic homepage, career portal, search-results page, talent-community form, or company homepage as a verified opening.
- Put generic career portals only in the earlier company pool and label them `关注入口`; put only specific, current JD/application pages in the live table.
- Prefer 12–20 verified or likely-live rows across priority geographies when the market actually offers them. Never pad the count with duplicates, stale posts, unrelated roles, or weak geographies; report a genuinely smaller set when evidence is limited.
- Exclude closed or expired roles from the live table. Mention a strategically important closure only in the pre-table market interpretation.
- If no verified live role is found, still end with the prescribed table and one explicit `未找到可核验在招岗位` row describing the search date and coverage.
- If current web access is unavailable, do not claim results are live. End with the table and mark verification status accordingly.

After drafting an industry report saved as Markdown, run:

```bash
python scripts/validate_report.py path/to/report.md
```

Fix every reported error before delivery.

## Make the decision useful

Always answer:

- Which industry-chain node is the best entry and why?
- Which companies are strong businesses but weak career fits for this user?
- Which companies offer the best overseas sales career value?
- Which roles are realistically enterable now?
- What would the user own after three years?
- What evidence would reverse the recommendation?

Never recommend a company merely because it is famous, listed, growing fast, or in a hot sector. Treat financial growth as a clue to expansion, then check cash collection, customer concentration, overseas momentum, product competitiveness, sales hiring, and the actual work.
