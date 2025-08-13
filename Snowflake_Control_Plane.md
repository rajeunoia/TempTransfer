h1. Snowflake Control Plane Capabilities — How They Map to Your Feature List

Below is a deep-dive mapping of each control-plane capability in your image to how Snowflake implements or enables it. For every section, I’ve included brief notes and reference links you can keep in Confluence.

⸻

h2. Unified API Gateway for Data Platforms

Snowflake does not ship a universal, cross-platform API gateway. Instead, it exposes multiple native APIs and lets you front your own services via cloud API gateways that Snowflake can call securely.
	•	Native Snowflake APIs: SQL API (REST), Snowpipe (REST), Snowpipe Streaming, drivers/SDKs (JDBC/ODBC/Python/Snowpark).
	•	Call external services from Snowflake: External Functions use an API INTEGRATION to call services behind AWS API Gateway / Azure API Management / GCP API Gateway; auth and endpoint policy sit in the integration.  ￼
	•	API lifecycle & catalog: You can catalog and govern these endpoints (and the tables/views that back them) with Horizon tags and policies; usage is visible via query history/access history.  ￼
	•	Metering/monetization: Usage of external functions and serverless features is metered as credits; monetization of apps/data is supported via Snowflake Marketplace & Native Apps (not an API gateway per se, but the supported model for productizing data/apps on Snowflake).  ￼

References
[External Functions overview|https://docs.snowflake.com/en/sql-reference/external-functions-introduction]  ￼
[Object Tagging (for catalog & governance)|https://docs.snowflake.com/en/user-guide/object-tagging/introduction]  ￼
[Horizon Catalog (governance & discovery umbrella)|https://docs.snowflake.com/en/user-guide/snowflake-horizon]  ￼

⸻

h2. FinOps & Cost Optimization

Snowflake provides native knobs for cost control, monitoring, and chargeback.
	•	Resource Monitors — set credit quotas with triggers (notify / suspend / suspend_immediate) at account or warehouse scope. Good for budgets, guardrails, and automated suspension.  ￼
	•	Warehouse policies — auto-suspend/resume, scaling policy, size tiers; analyze with ACCOUNT_USAGE/ORGANIZATION_USAGE views & Snowsight Usage pages.  ￼
	•	Tag-based cost allocation — create tags like cost_center or owner and attach them to warehouses, databases, schemas, etc.; join usage views with tag references for chargeback.  ￼

References
[Working with Resource Monitors|https://docs.snowflake.com/en/user-guide/resource-monitors]  ￼
[CREATE RESOURCE MONITOR (examples)|https://docs.snowflake.com/en/sql-reference/sql/create-resource-monitor]  ￼
[Object Tagging (cost/owner tagging)|https://docs.snowflake.com/en/user-guide/object-tagging/introduction]  ￼

⸻

h2. Unified Access Control & AuthZ

Snowflake is strongly RBAC-centric, with policy objects for ABAC-like behavior.
	•	RBAC: roles, privileges, future grants; administer at database/schema/object granularity.  ￼
	•	Data policies: Masking Policies (PII redaction, conditional masks) and Row Access Policies (predicate-based row filtering) bind to columns/tables and can leverage tags for policy application at scale.  ￼
	•	Identity/SSO: SAML 2.0 SSO, OAuth, SCIM provisioning (IdP-driven lifecycle and JIT-style enablement via IdP). Snowflake does not provide native “time-bound” grants; teams typically automate time-boxed access with tasks/procs that revoke grants on schedule (implementation pattern).  ￼

References
[Access Control Overview|https://docs.snowflake.com/en/user-guide/security-access-control-overview]  ￼
[Masking & Row Access Policies|https://docs.snowflake.com/en/user-guide/security-column-intro]  ￼
[SSO (SAML) / OAuth / SCIM|https://docs.snowflake.com/en/user-guide/security-fed-auth]  ￼

⸻

h2. Monitoring & Observability

First-class telemetry + SQL-native alerts and cloud notifications.
	•	Snowsight — query history, performance graphs, usage dashboards.  ￼
	•	SQL Alerts — define a condition and schedule, then notify (email, webhook via notification integrations) or trigger procedures.  ￼
	•	Notification Integrations — connect alerts/pipelines to AWS SNS / Azure Event Grid / GCP Pub/Sub for Slack/Teams/email or downstream automations.  ￼
	•	Event Tables — OpenTelemetry-modeled event store for logs/metrics/traces from UDFs, procedures, and services; query with SQL, apply RAP for secure access.  ￼

References
[Alerts|https://docs.snowflake.com/en/user-guide/alerts]  ￼
[Notification Integrations|https://docs.snowflake.com/en/user-guide/notifications-intro]  ￼
[Event Table Overview|https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up]  ￼

⸻

h2. Logging & Audit

Comprehensive account & access auditing—queryable in SQL.
	•	ACCESS_HISTORY — who read/wrote which objects (and even column-level lineage for writes).  ￼
	•	LOGIN_HISTORY — authentication events; join with user/session info for security analytics.  ￼
	•	ACCOUNT_USAGE & INFORMATION_SCHEMA views cover warehouse metering, query history, task/pipe history, etc.; data is system-managed and query-only, supporting audit workflows.  ￼

References
[Access History|https://docs.snowflake.com/en/user-guide/access-history]  ￼
[LOGIN_HISTORY|https://docs.snowflake.com/en/sql-reference/account-usage/login_history]  ￼
[ACCOUNT_USAGE schema|https://docs.snowflake.com/en/sql-reference/account-usage]  ￼

⸻

h2. Data Discovery

Discovery sits under Snowflake Horizon.*
	•	Universal Search — search across databases, schemas, tables, views, apps, listings.  ￼
	•	Sensitive Data Classification — auto/manual classification that applies system tags to columns; these tags drive downstream policies and reporting.  ￼
	•	Search Optimization — indexing-like service to speed selective/filtering queries (useful for discovery & point lookups across large tables).  ￼

References
[Horizon Catalog|https://docs.snowflake.com/en/user-guide/snowflake-horizon]  ￼
[Sensitive Data Classification (intro)|https://docs.snowflake.com/en/user-guide/classify-intro]  ￼
[Search Optimization Service|https://docs.snowflake.com/en/user-guide/search-optimization-service]  ￼

⸻

h2. Data Access Compliance Requests

Enforce access via policies; review via Horizon + Access History.
	•	Implement policy-as-code with masking policies, row access policies, and tags (e.g., sensitivity, residency). Use policy references & Horizon views to prove where policies apply.  ￼
	•	Approval workflows are typically built on top of Snowflake using alerts + notification integrations + procedures (e.g., create a ticket, then GRANT on approval). (Implementation pattern; not a native approval queue.)  ￼

References
[Masking/Row Access Policies|https://docs.snowflake.com/en/user-guide/security-column-intro]  ￼
[Object Tagging (apply compliance metadata)|https://docs.snowflake.com/en/user-guide/object-tagging/introduction]  ￼

⸻

h2. Integration Orchestration

Snowflake can schedule and trigger pipelines natively; you can also hand off to external orchestrators.
	•	Streams & Tasks — change data capture (+ DAGs with task graphs) and scheduled/triggered SQL or procedures.  ￼
	•	Dynamic Tables — declarative, target-lag driven pipelines (Snowflake manages refresh orchestration); lineage graphs in Snowsight.  ￼
	•	Snowpipe (auto-ingest) — event-driven loading on S3/Azure/GCS via cloud notifications.  ￼
	•	External Functions — orchestrate calls to external microservices/APIs as steps within SQL pipelines.  ￼

References
[Streams & Tasks|https://docs.snowflake.com/en/user-guide/data-pipelines-intro]  ￼
[Dynamic Tables|https://docs.snowflake.com/en/user-guide/dynamic-tables-about]  ￼
[Snowpipe Auto-ingest|https://docs.snowflake.com/en/user-guide/data-load-snowpipe-auto-s3]  ￼

⸻

h2. Cross-Platform Lineage

Native lineage inside Snowflake is now robust; for cross-platform lineage you typically integrate 3rd-party catalogs.
	•	In-platform lineage: Snowsight lineage UI + GET_LINEAGE() function; includes table/column/stage and ML objects (datasets, feature views, models).  ￼
	•	Access History gives column-level write lineage programmatically for impact analysis.  ￼
	•	Cross-platform: Tools like Alation, Atlan, etc., ingest Snowflake lineage and stitch with upstream ETL/BI (outside Snowflake scope).  ￼ ￼

References
[Data Lineage (Snowsight + GET_LINEAGE)|https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage]  ￼
[Release Notes — Data Lineage|https://docs.snowflake.com/en/release-notes/2024/other/2024-11-04-data-lineage]  ￼
[ML Lineage|https://docs.snowflake.com/en/developer-guide/snowflake-ml/ml-lineage]  ￼
[Access History (column lineage)|https://docs.snowflake.com/en/user-guide/access-history]  ￼

⸻

h2. Quality & Contract Enforcement

Snowflake offers policy objects, alerts, and Horizon “Data Quality” monitoring capabilities; hard relational constraints are evolving.
	•	Data Quality in Horizon — governance features include data quality monitoring (native metrics & monitors surfaced in Snowsight).  ￼
	•	SQL-based checks — implement via tasks/procs + alerts; write failures/threshold breaches to tables or event tables and notify Ops.  ￼
	•	Constraints: NOT NULL is enforced; PK/unique/foreign key enforcement has historically been informational, with selective enforcement progressing over recent releases—teams still rely on tests + alerts for promotion gates. (Check current release notes for your account’s region/edition.)  ￼

References
[Horizon governance overview (incl. DQ)|https://www.snowflake.com/en/blog/horizon-leading-governance-data-discovery/]  ￼
[Alerts (for DQ gates)|https://docs.snowflake.com/en/user-guide/alerts]  ￼
[Event Tables (for telemetry/DQ logs)|https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up]  ￼

⸻

h2. Integration with User Experience Portal

Snowsight is the native UX; Horizon unifies discovery/governance; Streamlit/Native Apps let you build your own portal.
	•	Snowsight — unified SQL/Notebooks, query monitoring, worksheets, dashboards; shared folders.  ￼
	•	Horizon in Snowsight — search, lineage, tags, classification, DQ in one place.  ￼
	•	Build your own portal — Streamlit in Snowflake and Native Apps to package + distribute internal apps with role-based access.  ￼

References
[Snowsight overview|https://docs.snowflake.com/en/user-guide/ui-snowsight]  ￼
[Horizon Catalog|https://docs.snowflake.com/en/user-guide/snowflake-horizon]  ￼

⸻

h2. Eventing & Data Operations

Event-driven pipelines, notifications, and first-class telemetry.
	•	Snowpipe auto-ingest — cloud-storage events trigger loads (S3/SNS/SQS, EventBridge, etc.).  ￼
	•	Alerts + Notification Integrations — conditions → actions (email/webhook/SNS/Event Grid/PubSub).  ￼
	•	Event Tables — collect logs/metrics/traces (OpenTelemetry model) for ops analytics and automated responses.  ￼
	•	Streams/Tasks & Dynamic Tables — trigger on change (CDC) or maintain declarative refresh SLAs with target lag.  ￼

References
[Snowpipe Auto-ingest|https://docs.snowflake.com/en/user-guide/data-load-snowpipe-auto-s3]  ￼
[Alerts & Notification Integrations|https://docs.snowflake.com/en/user-guide/alerts]  ￼
[Event Table Overview|https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up]  ￼

⸻

h2. Logging & Audit (Expanded quick-links)

{panel}
	•	[ACCOUNT_USAGE Overview|https://docs.snowflake.com/en/sql-reference/account-usage]  ￼
	•	[ACCESS_HISTORY|https://docs.snowflake.com/en/user-guide/access-history]  ￼
	•	[LOGIN_HISTORY|https://docs.snowflake.com/en/sql-reference/account-usage/login_history]  ￼
	•	[RESOURCE_MONITORS views|https://docs.snowflake.com/en/sql-reference/organization-usage/resource_monitors]  ￼
{panel}

⸻

h2. Notes & Gaps to Plan For
	•	Just-in-time / time-bound grants: No native “grant with expiry”; implement with Tasks + Alerts + stored procedures to revoke on schedule (IdP JIT handles auth, not Snowflake grants).  ￼
	•	Central API gateway: Use cloud API gateways; integrate with Snowflake via External Functions (API INTEGRATION).  ￼
	•	Cross-platform lineage: Use native lineage + Access History within Snowflake; stitch upstream/downstream with a catalog (Alation/Atlan/etc.) if you need end-to-end across tools.  ￼ ￼

⸻

h2. Appendix — Handy Links Block (copy/paste)

{code}
External Functions: https://docs.snowflake.com/en/sql-reference/external-functions-introduction
Horizon Catalog: https://docs.snowflake.com/en/user-guide/snowflake-horizon
Snowsight: https://docs.snowflake.com/en/user-guide/ui-snowsight
Resource Monitors: https://docs.snowflake.com/en/user-guide/resource-monitors
Object Tagging: https://docs.snowflake.com/en/user-guide/object-tagging/introduction
Sensitive Data Classification: https://docs.snowflake.com/en/user-guide/classify-intro
Snowpipe Auto-ingest: https://docs.snowflake.com/en/user-guide/data-load-snowpipe-auto-s3
Streams & Tasks: https://docs.snowflake.com/en/user-guide/data-pipelines-intro
Dynamic Tables: https://docs.snowflake.com/en/user-guide/dynamic-tables-about
Alerts: https://docs.snowflake.com/en/user-guide/alerts
Notification Integrations: https://docs.snowflake.com/en/user-guide/notifications-intro
Event Tables: https://docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up
Data Lineage (UI + GET_LINEAGE): https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage
Access History: https://docs.snowflake.com/en/user-guide/access-history
{code}

⸻

If you want, I can convert this into a Snowflake-ready checklist (SQL snippets + governance queries) for each capability and attach it to your Confluence page.
