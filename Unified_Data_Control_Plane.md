h1. Unified Data Control Plane – Executive Overview

h2. Vision
Create a *single, centralized control plane* that unifies governance, observability, orchestration, and access across diverse data platforms—without replacing native platform capabilities.  
This layer enforces *policies once*, gathers cross-platform telemetry, drives automation, and presents a consistent user experience.

---

h2. Scope
* *Data Lake*: AWS S3 with Glue Catalog & Lake Formation governance
* *Data Warehouse*: Snowflake with External Tables on S3 + Internal Catalog
* *Global Catalog*: Aggregates technical metadata and distribution information across all systems
* *Event Bus*: Normalizes data operation and activity events from all platforms

---

h2. Key Capabilities

# *FinOps & Cost Optimization*
** Unified cost tracking (storage, compute, egress) per domain/product/user
** Budgets, anomaly detection, optimization recommendations

# *Unified Access Control & AuthZ*
** Policy-as-code → compile to Snowflake/IAM/Lake Formation
** JIT, time-bound, and least-privilege access

# *Monitoring & Observability*
** Health model for datasets; SLOs with error budgets
** Freshness, volume, and failure rate tracking

# *Logging & Audit*
** Immutable logs of grants, changes, events, and access
** Evidence packs for audits

# *Data Discovery*
** Cross-platform catalog with taxonomy, sensitivity tags, SLAs, lineage

# *Data Access Compliance Requests*
** Policy-driven approvals with evidence trails
** Time-boxed access & auto-revocation

# *Integration Orchestration*
** Event-driven workflows; trigger native jobs/tasks
** Coordinate dependencies across platforms

# *Cross-Platform Lineage*
** End-to-end lineage for impact analysis & change propagation

# *Quality & Contract Enforcement*
** Schema compatibility checks, quality rules, promotion gates

# *User Experience Portal*
** Self-service discovery, access, lineage, cost, health in one UI

# *Eventing on Data Operations*
** Capture, normalize, and route events from all platforms
** Drive automation and alerts from operations

---

h2. Eventing Layer
*Sources*: AWS S3, Glue, Lake Formation, Snowflake, Global Catalog

*Event Types:*
* Schema changes
* Data quality breaches
* Access changes
* Cost anomalies
* Lifecycle state changes (archival, tiering)
* SLA breaches

*Actions:*
* Trigger workflows/playbooks
* Notify consumers/producers
* Auto-remediate or revoke access

---

h2. Benefits
* *Consistent Governance*: Define once, enforce everywhere
* *Operational Efficiency*: Faster onboarding, reduced manual work
* *Trust & Transparency*: Clear lineage, SLAs, and quality signals
* *Cost Control*: Full spend visibility and optimization levers
* *Scalable Integration*: Extend via adapters for new platforms

---

h2. Architecture Diagram
!unified_data_control_plane_v2.png!

