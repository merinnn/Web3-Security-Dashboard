# Matrix SecOps: Autonomous Web3 Attack & Defense Arena 👁️⚡

## 📌 Overview
**Matrix SecOps** is an event-driven Security Operations Center (SOC) dashboard and self-healing vulnerability remediation platform built to monitor decentralized infrastructure layers. 

The application architecture establishes a closed-loop **Dual-Agent Competition Arena**. An adversarial agent continually scans configuration paths for structural code vulnerabilities (such as state-sequencing flaws in Solidity), launching live mock exploits. Simultaneously, a defensive guardian agent intercepts threat signatures, logs anomalies, and applies an atomic secure refactor directly to the filesystem—healing the code in real time while streaming live data pipelines smoothly to the user interface.

---

## 📸 Interface Showcases

### 1. Real-Time SecOps Dashboard Monitor
The central operations desk handles live telemetry data parsing, visual gas velocity curve plots using Chart.js, and concurrent transaction ingestion.
![Live Monitor Panel](Screenshot%202026-06-05%20181621.png)

### 2. Live Security Activity Stream
An instantaneous console capture detailing the real-time interaction between the adversarial execution layer and the autonomous guardian refactor iterations.
![Activity Stream Component](Screenshot%202026-06-05%20181634.png)

### 3. VAPT Smart Contract Directory
Toggling the navigation path switches views natively to inspect audited contract arrays, tracking fluid security metric shifts from vulnerable states up to 100% patched structures.
![Contract Audits Panel](Screenshot%202026-06-05%20181648.png)

### 4. Incident Log Archive Index
A decoupled data caching ledger tracking distinct historical threats blocked by the defensive engine, ensuring persistent compliance auditing.
![Incidents Log Tab](Screenshot%202026-06-05%20181701.png)

---

## 🏗️ Core Engineering Milestones
* **Event-Driven Data Pipeline:** Engineered an atomic asynchronous file orchestration workflow where backend processing cycles output uniform JSON tracking layers seamlessly consumed by frontend polling logic.
* **Single-Page Application (SPA) Routing:** Designed a responsive navigation framework utilizing native vanilla JavaScript view-switching to cycle layout components instantly without clearing browser tab execution states.
* **Cyberpunk Matrix UI Layout:** Built a high-end, cohesive emerald-neon user interface layout optimizing visual data densities, CSS custom variable tokens, and dark-mode readability standards.

---

## 📁 Repository Map
```text
Web3-Security-Dashboard/
├── contracts/                   # Monitored smart contract directory
│   └── Vault.sol                # Target application asset layer (Autopatched)
├── public/                      # User interface microservice
│   ├── telemetry.json           # Unified event-driven data pipeline exchange matrix
│   └── index.html               # SPA responsive Matrix SecOps dashboard code
└── scripts/                     # Multi-agent simulation loop orchestrators
    └── arena_orchestrator.py    # Automated adversarial attack & defense runner
```

## 🛠️ Local Initialization
Prerequisites
Ensure your workstation possesses standard Python 3 execution frameworks:

Bash
pip install flask sqlite3

## Launching the Pipeline Environment
Deploy the local file-serving network module background node:

Bash
python -m http.server --directory public 8080 &
Initiate the dual-agent attack/defense simulation runner:

Bash
python scripts/arena_orchestrator.py &
Navigate your browser core to view the live dashboard: http://localhost:8080
