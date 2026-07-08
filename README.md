<div align="center">
    <h1>Awesome Sub-Agents</h1>
    <strong>An Autohand-curated collection of 172 markdown sub-agents across 13 categories.</strong>
    <br />
    <br />
</div>

   
<div align="center">
    
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Subagent Count](https://img.shields.io/badge/subagents-172-blue?style=classic)
[![Last Update](https://img.shields.io/github/last-commit/autohandai/awesome-sub-agents?label=Last%20update&style=classic)](https://github.com/autohandai/awesome-sub-agents)

</div>

<br />

# Awesome Sub-Agents

This repository is a curated collection of Autohand Code sub-agents: specialized AI assistants designed for specific development tasks. The agent files are written in Autohand markdown format and organized by practical development domain.

This Autohand collection is based on [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) at commit `ca0d57bde60ed56a415cd4b2319c261a13b46689`. The original project is MIT licensed; see [NOTICE.md](NOTICE.md) and [LICENSE](LICENSE).

## Installation

Use Autohand custom agent directories:

- `~/.autohand/agents/` for global agents available to Autohand Code.
- `--agents <path>` to point one session at an external agent directory.
- The Autohand Code catalog installer can install agents from this repository automatically when available.

1. Clone this repository.
2. Copy the `.md` agent files you want into one of the directories above.
3. Restart or refresh your Autohand Code session if needed.
4. Delegate explicitly in prompts or use Autohand Code's catalog installer when available.

Examples:
```bash
mkdir -p ~/.autohand/agents
cp categories/01-core-development/backend-developer.md ~/.autohand/agents/
```

```bash
autohand --agents ./categories/04-quality-security
```

### Subagent Storage Locations

| Type | Path | Availability | Precedence |
|------|------|--------------|------------|
| Global Subagents | `~/.autohand/agents/` | All Autohand Code projects | Standard |
| External Subagents | `--agents <path>` or configured external path | Current session/config | Session/config scoped |

Note: Session-injected agents and project-generated agents can override file-based agents with the same name in Autohand Code.

## Registry

Autohand Code reads [registry.json](registry.json) to search and install agents from this catalog without cloning the repository. The registry is generated from agent frontmatter and includes each agent's name, description, category, path, tools, and model.

When changing agents, regenerate and validate the registry:

```bash
python3 scripts/generate_registry.py
python3 scripts/validate_agents.py
```

## Subagent Structure

Each subagent uses Autohand's markdown agent format:

```markdown
---
description: When this agent should be invoked
tools: read_file, fff_grep, fff_find
model: gpt-5.3-codex-spark
---

You are a [role description and expertise areas]...

[Agent-specific checklists, patterns, and guidelines]...
```

### Smart Model Routing

Each subagent includes a `model` field that automatically routes it to the right model -- balancing quality and cost:

| Model | When It's Used | Examples |
|-------|----------------|----------|
| `gpt-5.4` | Deep reasoning -- architecture reviews, security audits, financial logic | `security-auditor`, `architect-reviewer`, `fintech-engineer` |
| `gpt-5.3-codex-spark` | Fast scanning, synthesis, and lighter research tasks | `search-specialist`, `docs-researcher`, `agent-installer` |

### Sandbox Mode Philosophy

Each subagent declares the tools it can use in frontmatter:
- **Read-only agents** (reviewers, auditors): `read_file, fff_grep, fff_find`
- **Workspace-write agents** (developers, engineers): `read_file, fff_grep, fff_find, apply_patch, search_replace, run_command`



## Categories

### [01. Core Development](categories/01-core-development/)

Essential development subagents for everyday coding tasks.

- [**api-designer**](categories/01-core-development/api-designer.md) - REST and GraphQL API architect
- [**backend-developer**](categories/01-core-development/backend-developer.md) - Server-side expert for scalable APIs
- [**code-mapper**](categories/01-core-development/code-mapper.md) - Code path mapping and ownership boundary analysis
- [**design-bridge**](categories/01-core-development/design-bridge.md) - Translates DESIGN.md specs into implementation-ready UI instructions
- [**electron-pro**](categories/01-core-development/electron-pro.md) - Desktop application expert
- [**frontend-developer**](categories/01-core-development/frontend-developer.md) - UI/UX specialist for React, Vue, and Angular
- [**fullstack-developer**](categories/01-core-development/fullstack-developer.md) - End-to-end feature development
- [**graphql-architect**](categories/01-core-development/graphql-architect.md) - GraphQL schema and federation expert
- [**microservices-architect**](categories/01-core-development/microservices-architect.md) - Distributed systems designer
- [**mobile-developer**](categories/01-core-development/mobile-developer.md) - Cross-platform mobile specialist
- [**ui-designer**](categories/01-core-development/ui-designer.md) - Visual design and interaction specialist
- [**ui-fixer**](categories/01-core-development/ui-fixer.md) - Smallest safe patch for reproduced UI issues
- [**websocket-engineer**](categories/01-core-development/websocket-engineer.md) - Real-time communication specialist

### [02. Language Specialists](categories/02-language-specialists/)

Language-specific experts with deep framework knowledge.
- [**angular-architect**](categories/02-language-specialists/angular-architect.md) - Angular 15+ enterprise patterns expert
- [**cpp-pro**](categories/02-language-specialists/cpp-pro.md) - C++ performance expert
- [**csharp-developer**](categories/02-language-specialists/csharp-developer.md) - .NET ecosystem specialist
- [**django-developer**](categories/02-language-specialists/django-developer.md) - Django 4+ web development expert
- [**dotnet-core-expert**](categories/02-language-specialists/dotnet-core-expert.md) - .NET 8 cross-platform specialist
- [**dotnet-framework-4.8-expert**](categories/02-language-specialists/dotnet-framework-4.8-expert.md) - .NET Framework legacy enterprise specialist
- [**elixir-expert**](categories/02-language-specialists/elixir-expert.md) - Elixir and OTP fault-tolerant systems expert
- [**erlang-expert**](categories/02-language-specialists/erlang-expert.md) - Erlang/OTP and rebar3 engineering expert
- [**expo-react-native-expert**](categories/02-language-specialists/expo-react-native-expert.md) - Expo and React Native mobile development expert
- [**fastapi-developer**](categories/02-language-specialists/fastapi-developer.md) - Modern async Python API framework expert
- [**flutter-expert**](categories/02-language-specialists/flutter-expert.md) - Flutter 3+ cross-platform mobile expert
- [**golang-pro**](categories/02-language-specialists/golang-pro.md) - Go concurrency specialist
- [**java-architect**](categories/02-language-specialists/java-architect.md) - Enterprise Java expert
- [**javascript-pro**](categories/02-language-specialists/javascript-pro.md) - JavaScript development expert
- [**kotlin-specialist**](categories/02-language-specialists/kotlin-specialist.md) - Modern JVM language expert
- [**laravel-specialist**](categories/02-language-specialists/laravel-specialist.md) - Laravel 10+ PHP framework expert
- [**symfony-specialist**](categories/02-language-specialists/symfony-specialist.md) - Symfony application and Doctrine specialist
- [**nextjs-developer**](categories/02-language-specialists/nextjs-developer.md) - Next.js 14+ full-stack specialist
- [**node-specialist**](categories/02-language-specialists/node-specialist.md) - Node.js backend specialist
- [**php-pro**](categories/02-language-specialists/php-pro.md) - PHP web development expert
- [**powershell-5.1-expert**](categories/02-language-specialists/powershell-5.1-expert.md) - Windows PowerShell 5.1 and full .NET Framework automation specialist
- [**powershell-7-expert**](categories/02-language-specialists/powershell-7-expert.md) - Cross-platform PowerShell 7+ automation and modern .NET specialist
- [**python-pro**](categories/02-language-specialists/python-pro.md) - Python ecosystem master
- [**rails-expert**](categories/02-language-specialists/rails-expert.md) - Rails 8.1 rapid development expert
- [**react-specialist**](categories/02-language-specialists/react-specialist.md) - React 18+ modern patterns expert
- [**rust-engineer**](categories/02-language-specialists/rust-engineer.md) - Systems programming expert
- [**spring-boot-engineer**](categories/02-language-specialists/spring-boot-engineer.md) - Spring Boot 3+ microservices expert
- [**sql-pro**](categories/02-language-specialists/sql-pro.md) - Database query expert
- [**swift-expert**](categories/02-language-specialists/swift-expert.md) - iOS and macOS specialist
- [**typescript-pro**](categories/02-language-specialists/typescript-pro.md) - TypeScript specialist
- [**vue-expert**](categories/02-language-specialists/vue-expert.md) - Vue 3 Composition API expert


### [03. Infrastructure](categories/03-infrastructure/)

DevOps, cloud, and deployment specialists.

- [**azure-infra-engineer**](categories/03-infrastructure/azure-infra-engineer.md) - Azure infrastructure and Az PowerShell automation expert
- [**cloud-architect**](categories/03-infrastructure/cloud-architect.md) - AWS/GCP/Azure specialist
- [**database-administrator**](categories/03-infrastructure/database-administrator.md) - Database management expert
- [**deployment-engineer**](categories/03-infrastructure/deployment-engineer.md) - Deployment automation specialist
- [**devops-engineer**](categories/03-infrastructure/devops-engineer.md) - CI/CD and automation expert
- [**devops-incident-responder**](categories/03-infrastructure/devops-incident-responder.md) - DevOps incident management
- [**docker-expert**](categories/03-infrastructure/docker-expert.md) - Docker containerization and optimization expert
- [**incident-responder**](categories/03-infrastructure/incident-responder.md) - System incident response expert
- [**kubernetes-specialist**](categories/03-infrastructure/kubernetes-specialist.md) - Container orchestration master
- [**network-engineer**](categories/03-infrastructure/network-engineer.md) - Network infrastructure specialist
- [**platform-engineer**](categories/03-infrastructure/platform-engineer.md) - Platform architecture expert
- [**security-engineer**](categories/03-infrastructure/security-engineer.md) - Infrastructure security specialist
- [**sre-engineer**](categories/03-infrastructure/sre-engineer.md) - Site reliability engineering expert
- [**terraform-engineer**](categories/03-infrastructure/terraform-engineer.md) - Infrastructure as Code expert
- [**terragrunt-expert**](categories/03-infrastructure/terragrunt-expert.md) - Terragrunt orchestration and DRY IaC specialist
- [**windows-infra-admin**](categories/03-infrastructure/windows-infra-admin.md) - Active Directory, DNS, DHCP, and GPO automation specialist

<details>
<summary><b>04. Quality & Security</b> — Testing, security, and code quality experts (19 agents)</summary>

### [04. Quality & Security](categories/04-quality-security/)

- [**accessibility-tester**](categories/04-quality-security/accessibility-tester.md) - A11y compliance expert
- [**ad-security-reviewer**](categories/04-quality-security/ad-security-reviewer.md) - Active Directory security and GPO audit specialist
- [**ai-writing-auditor**](categories/04-quality-security/ai-writing-auditor.md) - AI writing pattern auditor and rewriter
- [**architect-reviewer**](categories/04-quality-security/architect-reviewer.md) - Architecture review specialist
- [**browser-debugger**](categories/04-quality-security/browser-debugger.md) - Browser-based reproduction and client-side debugging
- [**chaos-engineer**](categories/04-quality-security/chaos-engineer.md) - System resilience testing expert
- [**code-reviewer**](categories/04-quality-security/code-reviewer.md) - Code quality guardian
- [**compliance-auditor**](categories/04-quality-security/compliance-auditor.md) - Regulatory compliance expert
- [**debugger**](categories/04-quality-security/debugger.md) - Advanced debugging specialist
- [**error-detective**](categories/04-quality-security/error-detective.md) - Error analysis and resolution expert
- [**gdpr-ccpa-compliance**](categories/04-quality-security/gdpr-ccpa-compliance.md) - GDPR and CCPA privacy compliance specialist
- [**penetration-tester**](categories/04-quality-security/penetration-tester.md) - Ethical hacking specialist
- [**performance-engineer**](categories/04-quality-security/performance-engineer.md) - Performance optimization expert
- [**powershell-security-hardening**](categories/04-quality-security/powershell-security-hardening.md) - PowerShell security hardening and compliance specialist
- [**qa-expert**](categories/04-quality-security/qa-expert.md) - Test automation specialist
- [**reviewer**](categories/04-quality-security/reviewer.md) - PR-style review for correctness, security, and regressions
- [**security-auditor**](categories/04-quality-security/security-auditor.md) - Security vulnerability expert
- [**test-automator**](categories/04-quality-security/test-automator.md) - Test automation framework expert
- [**ui-ux-tester**](categories/04-quality-security/ui-ux-tester.md) - Exhaustive UI/UX functional testing specialist

</details>

<details>
<summary><b>05. Data & AI</b> — Data engineering, ML, and AI specialists (13 agents)</summary>

### [05. Data & AI](categories/05-data-ai/)

- [**ai-engineer**](categories/05-data-ai/ai-engineer.md) - AI system design and deployment expert
- [**data-analyst**](categories/05-data-ai/data-analyst.md) - Data insights and visualization specialist
- [**data-engineer**](categories/05-data-ai/data-engineer.md) - Data pipeline architect
- [**data-scientist**](categories/05-data-ai/data-scientist.md) - Analytics and insights expert
- [**database-optimizer**](categories/05-data-ai/database-optimizer.md) - Database performance specialist
- [**llm-architect**](categories/05-data-ai/llm-architect.md) - Large language model architect
- [**machine-learning-engineer**](categories/05-data-ai/machine-learning-engineer.md) - Machine learning systems expert
- [**ml-engineer**](categories/05-data-ai/ml-engineer.md) - Machine learning specialist
- [**mlops-engineer**](categories/05-data-ai/mlops-engineer.md) - MLOps and model deployment expert
- [**nlp-engineer**](categories/05-data-ai/nlp-engineer.md) - Natural language processing expert
- [**postgres-pro**](categories/05-data-ai/postgres-pro.md) - PostgreSQL database expert
- [**prompt-engineer**](categories/05-data-ai/prompt-engineer.md) - Prompt optimization specialist
- [**reinforcement-learning-engineer**](categories/05-data-ai/reinforcement-learning-engineer.md) - Reinforcement learning and decision systems expert

</details>

<details>
<summary><b>06. Developer Experience</b> — Tooling and developer productivity experts (14 agents)</summary>

### [06. Developer Experience](categories/06-developer-experience/)

- [**build-engineer**](categories/06-developer-experience/build-engineer.md) - Build system specialist
- [**cli-developer**](categories/06-developer-experience/cli-developer.md) - Command-line tool creator
- [**dependency-manager**](categories/06-developer-experience/dependency-manager.md) - Package and dependency specialist
- [**documentation-engineer**](categories/06-developer-experience/documentation-engineer.md) - Technical documentation expert
- [**dx-optimizer**](categories/06-developer-experience/dx-optimizer.md) - Developer experience optimization specialist
- [**git-workflow-manager**](categories/06-developer-experience/git-workflow-manager.md) - Git workflow and branching expert
- [**legacy-modernizer**](categories/06-developer-experience/legacy-modernizer.md) - Legacy code modernization specialist
- [**mcp-developer**](categories/06-developer-experience/mcp-developer.md) - Model Context Protocol specialist
- [**powershell-module-architect**](categories/06-developer-experience/powershell-module-architect.md) - PowerShell module and profile architecture specialist
- [**powershell-ui-architect**](categories/06-developer-experience/powershell-ui-architect.md) - PowerShell UI/UX specialist for WinForms, WPF, Metro frameworks, and TUIs
- [**readme-generator**](categories/06-developer-experience/readme-generator.md) - Maintainer-ready README generator with zero hallucination
- [**refactoring-specialist**](categories/06-developer-experience/refactoring-specialist.md) - Code refactoring expert
- [**slack-expert**](categories/06-developer-experience/slack-expert.md) - Slack platform and @slack/bolt specialist
- [**tooling-engineer**](categories/06-developer-experience/tooling-engineer.md) - Developer tooling specialist

</details>

<details>
<summary><b>07. Specialized Domains</b> — Domain-specific technology experts (14 agents)</summary>

### [07. Specialized Domains](categories/07-specialized-domains/)

- [**api-documenter**](categories/07-specialized-domains/api-documenter.md) - API documentation specialist
- [**blockchain-developer**](categories/07-specialized-domains/blockchain-developer.md) - Web3 and crypto specialist
- [**embedded-systems**](categories/07-specialized-domains/embedded-systems.md) - Embedded and real-time systems expert
- [**fintech-engineer**](categories/07-specialized-domains/fintech-engineer.md) - Financial technology specialist
- [**game-developer**](categories/07-specialized-domains/game-developer.md) - Game development expert
- [**healthcare-admin**](categories/07-specialized-domains/healthcare-admin.md) - Healthcare administration, revenue cycle, and compliance specialist
- [**hipaa-compliance**](categories/07-specialized-domains/hipaa-compliance.md) - HIPAA compliance specialist for healthcare SaaS vendors
- [**iot-engineer**](categories/07-specialized-domains/iot-engineer.md) - IoT systems developer
- [**m365-admin**](categories/07-specialized-domains/m365-admin.md) - Microsoft 365, Exchange Online, Teams, and SharePoint administration specialist
- [**mobile-app-developer**](categories/07-specialized-domains/mobile-app-developer.md) - Mobile application specialist
- [**payment-integration**](categories/07-specialized-domains/payment-integration.md) - Payment systems expert
- [**quant-analyst**](categories/07-specialized-domains/quant-analyst.md) - Quantitative analysis specialist
- [**risk-manager**](categories/07-specialized-domains/risk-manager.md) - Risk assessment and management expert
- [**seo-specialist**](categories/07-specialized-domains/seo-specialist.md) - Search engine optimization expert

</details>

<details>
<summary><b>08. Business & Product</b> — Product management and business analysis (16 agents)</summary>

### [08. Business & Product](categories/08-business-product/)

- [**assumption-mapping**](categories/08-business-product/assumption-mapping.md) - Product assumption risk and validation specialist
- [**backlog-grooming**](categories/08-business-product/backlog-grooming.md) - Agile backlog refinement specialist
- [**business-analyst**](categories/08-business-product/business-analyst.md) - Requirements specialist
- [**content-marketer**](categories/08-business-product/content-marketer.md) - Content marketing specialist
- [**content-quality-editor**](categories/08-business-product/content-quality-editor.md) - AI content quality and humanization specialist
- [**customer-success-manager**](categories/08-business-product/customer-success-manager.md) - Customer success expert
- [**growth-loops**](categories/08-business-product/growth-loops.md) - Growth loop and PLG mechanics specialist
- [**legal-advisor**](categories/08-business-product/legal-advisor.md) - Legal and compliance specialist
- [**license-engineer**](categories/08-business-product/license-engineer.md) - Software licensing and compliance systems specialist
- [**product-manager**](categories/08-business-product/product-manager.md) - Product strategy expert
- [**project-manager**](categories/08-business-product/project-manager.md) - Project management specialist
- [**sales-engineer**](categories/08-business-product/sales-engineer.md) - Technical sales expert
- [**scrum-master**](categories/08-business-product/scrum-master.md) - Agile methodology expert
- [**technical-writer**](categories/08-business-product/technical-writer.md) - Technical documentation specialist
- [**ux-researcher**](categories/08-business-product/ux-researcher.md) - User research expert
- [**wordpress-master**](categories/08-business-product/wordpress-master.md) - WordPress development and optimization expert

</details>

<details>
<summary><b>09. Meta & Orchestration</b> — Agent coordination and meta-programming (12 agents)</summary>

### [09. Meta & Orchestration](categories/09-meta-orchestration/)

- [**agent-installer**](categories/09-meta-orchestration/agent-installer.md) - Browse and install agents from this repository via GitHub
- [**agent-organizer**](categories/09-meta-orchestration/agent-organizer.md) - Multi-agent coordinator
- [**codebase-orchestrator**](categories/09-meta-orchestration/codebase-orchestrator.md) - Repo-wide refactor governance with approval gates
- [**context-manager**](categories/09-meta-orchestration/context-manager.md) - Context optimization expert
- [**error-coordinator**](categories/09-meta-orchestration/error-coordinator.md) - Error handling and recovery specialist
- [**it-ops-orchestrator**](categories/09-meta-orchestration/it-ops-orchestrator.md) - IT operations workflow orchestration specialist
- [**knowledge-synthesizer**](categories/09-meta-orchestration/knowledge-synthesizer.md) - Knowledge aggregation expert
- [**multi-agent-coordinator**](categories/09-meta-orchestration/multi-agent-coordinator.md) - Advanced multi-agent orchestration
- [**performance-monitor**](categories/09-meta-orchestration/performance-monitor.md) - Agent performance optimization
- [**pied-piper**](https://github.com/sathish316/pied-piper/) - Orchestrate Team of AI Subagents for repetitive SDLC workflows
- [**task-distributor**](categories/09-meta-orchestration/task-distributor.md) - Task allocation specialist
- [**workflow-orchestrator**](categories/09-meta-orchestration/workflow-orchestrator.md) - Complex workflow automation

</details>

<details>
<summary><b>10. Research & Analysis</b> — Research, search, and analysis specialists (12 agents)</summary>

### [10. Research & Analysis](categories/10-research-analysis/)

- [**ab-test-analysis**](categories/10-research-analysis/ab-test-analysis.md) - A/B test interpretation and ship/no-ship decisions
- [**cohort-analysis**](categories/10-research-analysis/cohort-analysis.md) - Retention, cohort behavior, and activation-metric analysis
- [**competitive-analyst**](categories/10-research-analysis/competitive-analyst.md) - Competitive intelligence specialist
- [**data-researcher**](categories/10-research-analysis/data-researcher.md) - Data discovery and analysis expert
- [**docs-researcher**](categories/10-research-analysis/docs-researcher.md) - Documentation-backed API and framework verification
- [**first-principles-thinking**](categories/10-research-analysis/first-principles-thinking.md) - Assumption-challenging, first-principles problem solving
- [**market-researcher**](categories/10-research-analysis/market-researcher.md) - Market analysis and consumer insights
- [**project-idea-validator**](categories/10-research-analysis/project-idea-validator.md) - Brutal idea pressure-tester and go/no-go strategist
- [**research-analyst**](categories/10-research-analysis/research-analyst.md) - Comprehensive research specialist
- [**scientific-literature-researcher**](categories/10-research-analysis/scientific-literature-researcher.md) - Evidence-grounded research from published scientific studies
- [**search-specialist**](categories/10-research-analysis/search-specialist.md) - Advanced information retrieval expert
- [**trend-analyst**](categories/10-research-analysis/trend-analyst.md) - Emerging trends and forecasting expert

</details>

<details>
<summary><b>11. AI Governance & Safety</b> - Governance, guardrails, and trustworthy AI specialists (4 agents)</summary>

### [11. AI Governance & Safety](categories/11-ai-governance-safety/)

- [**ai-governance-auditor**](categories/11-ai-governance-safety/ai-governance-auditor.md) - AI governance controls and deployment readiness reviewer
- [**model-risk-manager**](categories/11-ai-governance-safety/model-risk-manager.md) - Model failure-mode prioritization and mitigation specialist
- [**policy-guardrail-designer**](categories/11-ai-governance-safety/policy-guardrail-designer.md) - Prompt, tool, and workflow guardrail designer
- [**responsible-ai-reviewer**](categories/11-ai-governance-safety/responsible-ai-reviewer.md) - Fairness, misuse, transparency, and oversight reviewer

</details>

<details>
<summary><b>12. Platform Engineering & IDP</b> - Internal developer platform and golden-path specialists (4 agents)</summary>

### [12. Platform Engineering & IDP](categories/12-platform-engineering-idp/)

- [**backstage-specialist**](categories/12-platform-engineering-idp/backstage-specialist.md) - Backstage catalog, templates, and portal specialist
- [**golden-path-designer**](categories/12-platform-engineering-idp/golden-path-designer.md) - Opinionated self-service workflow designer
- [**idp-architect**](categories/12-platform-engineering-idp/idp-architect.md) - Internal developer platform architecture specialist
- [**platform-product-manager**](categories/12-platform-engineering-idp/platform-product-manager.md) - Platform roadmap, adoption, and success-metrics specialist

</details>

<details>
<summary><b>13. LLMOps, Evals & Observability</b> - Production AI quality and runtime visibility specialists (4 agents)</summary>

### [13. LLMOps, Evals & Observability](categories/13-llmops-evals-observability/)

- [**ai-observability-engineer**](categories/13-llmops-evals-observability/ai-observability-engineer.md) - AI-native traces, metrics, and logging specialist
- [**eval-engineer**](categories/13-llmops-evals-observability/eval-engineer.md) - Prompt, tool, and workflow evaluation specialist
- [**hallucination-investigator**](categories/13-llmops-evals-observability/hallucination-investigator.md) - Factuality and context-breakdown root-cause investigator
- [**prompt-regression-tester**](categories/13-llmops-evals-observability/prompt-regression-tester.md) - Regression-suite designer for AI behavior changes

</details>

## Understanding Subagents

Subagents are specialized AI assistants that enhance Autohand Code by providing task-specific expertise. They act as dedicated helpers that Autohand Code can call upon when encountering particular types of work.

### What Makes Subagents Special?

**Independent Context Windows**
Every subagent operates within its own isolated context space, preventing cross-contamination between different tasks and maintaining clarity in the primary conversation thread.

**Domain-Specific Intelligence**
Subagents come equipped with carefully crafted instructions tailored to their area of expertise, resulting in superior performance on specialized tasks.

**Shared Across Projects**
After creating a subagent, you can utilize it throughout various projects and distribute it among team members to ensure consistent development practices.

**Explicit Delegation**
Autohand Code can use installed subagents through its agent and team tools. Use explicit delegation prompts to specify which agents to spawn, how to divide the work, and what shape the result should take.

### Core Advantages

- **Memory Efficiency**: Isolated contexts prevent the main conversation from becoming cluttered with task-specific details
- **Enhanced Accuracy**: Specialized prompts and configurations lead to better results in specific domains
- **Workflow Consistency**: Team-wide subagent sharing ensures uniform approaches to common tasks
- **Autohand-Native**: Uses markdown agent files loaded directly by Autohand Code

### Example Workflows

**PR review workflow:**
```text
Review this branch with parallel subagents. Have reviewer look for correctness, security, and missing tests. Have docs_researcher verify the framework APIs this patch depends on. Wait for both and summarize the findings with file references.
```

**Bug investigation workflow:**
```text
Investigate the broken settings flow. Have code_mapper trace the owning code paths, browser_debugger reproduce the bug in the browser, and frontend_developer propose the smallest fix after the failure is understood. Wait for the read-heavy agents first, then continue.
```

**Repo exploration and planning workflow:**
```text
Use search_specialist to locate the code related to payment retries, knowledge_synthesizer to summarize the current design, and refactoring_specialist to propose a minimal refactor plan. Return a concrete action list.
```
## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Submit new subagents via PR
- Improve existing definitions
- Report issues and bugs


## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of subagent definitions contributed by both the maintainers and the community. All subagents are provided "as is" without warranty. We do not audit or guarantee the security or correctness of any subagent. Review before use, the maintainers accept no liability for any issues arising from their use.

If you find an issue with a listed subagent or want your contribution removed, please open an issue in this repository and we'll address it promptly.
