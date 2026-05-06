# Sovereign Core Execution Layer

A unified orchestration layer that integrates multiple subsystems into a single deterministic execution pipeline with strict contract enforcement.

---

## 🚀 Overview

The **Sovereign Core Execution Layer** connects independent systems into one unified and deterministic flow:

**Sutradhara → DGIC → PDE → RAJYA → Sarathi → Core**

It ensures:

* Deterministic execution
* Strict contract validation
* Immutable data flow (append-only pipeline)
* Full observability and traceability

---

## 🧩 System Architecture

| Layer             | Responsibility       |
| ----------------- | -------------------- |
| Sutradhara        | Input (KSML)         |
| DGIC              | Reasoning Engine     |
| PDE               | Recommendation Layer |
| RAJYA             | Validation Authority |
| Sarathi           | Token Enforcement    |
| Core              | Execution Engine     |
| Integration Layer | Orchestration        |

---

## 🔁 Execution Flow

1. Validate execution contract

2. Call DGIC → generate reasoning

3. Call PDE → generate recommendation

4. Call RAJYA → validation decision

   * **REJECT** → stop execution
   * **APPROVED** → continue

5. Generate Sarathi token

6. Execute Core

7. Emit telemetry

8. Return final response

---

## 📦 Execution Object (Immutable Contract)

```json
{
  "execution_id": "string",
  "ksml_input": {},
  "dgic_output": null,
  "pde_output": null,
  "rajya_verdict": null,
  "sarathi_token": null,
  "enforcement_result": null
}
```

### 🔒 Contract Rules

* Same object flows across all layers
* `execution_id` must remain constant
* No mutation allowed
* Only append new fields
* Contract validation at every stage
* Any violation → **HARD FAIL**

---

## 📁 Project Structure

```
sovereign_core/
│
├── entry/
│   └── sovereign_core_entry.py
│
├── contract/
│   └── execution_contract_validator.py
│
├── harness/
│   └── run_sovereign_core.py
│
├── docs/
│   ├── sovereign_core_flow_map.md
│   ├── REVIEW_PACKET.md
│   └── execution_output.md
│
├── logs/
│   └── execution_logs.json
│
└── README.md
```

---

## ▶️ How to Run

```bash
python harness/run_sovereign_core.py
```

---

## ✅ Execution Results

### ✔ Approved Case

* Full pipeline executed (DGIC → PDE → RAJYA → Sarathi → Core)
* Token generated successfully
* Core execution completed
* Final enforcement result returned

### ❌ Reject Case

* Execution stopped at RAJYA
* No token generated
* No Core execution
* Telemetry emitted

📌 Full outputs available in:

* `docs/execution_output.md`
* `logs/execution_logs.json`

---

## 📊 Observability

* Contract validation logs at each step
* execution_id trace continuity across all layers
* Progressive state visibility (append-only proof)
* Clear execution flow tracking

---

## 📡 Telemetry

Telemetry is emitted after:

* Successful execution
* RAJYA rejection

Used for:

* Monitoring
* Debugging
* System health tracking

---

## 🛡️ Key Guarantees

* Deterministic execution
* Single entry point
* No duplicate logic
* Strict contract enforcement
* No execution without RAJYA approval
* No execution without Sarathi token
* Immutable data pipeline

---

## 🔧 Technologies Used

* Python 3
* JSON-based contract system
* Modular orchestration architecture

---

## 📌 Status

* ✅ Fully functional
* ✅ Tested (Approved + Reject flows)
* ✅ Contract enforced
* ✅ Integration-ready

---

