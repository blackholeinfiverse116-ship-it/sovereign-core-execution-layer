# Sovereign Core Execution Layer

A unified orchestration layer that integrates multiple subsystems into a single deterministic execution pipeline with strict contract enforcement.

---

## 🚀 Overview

The Sovereign Core Execution Layer connects all independent systems into one unified flow:

**Sutradhara → DGIC → PDE → RAJYA → Sarathi → Core**

It ensures:

* Deterministic execution
* Strict contract validation
* No data mutation (append-only pipeline)
* Full observability and traceability

---

## 🧩 System Architecture

| Layer             | Responsibility       |
| ----------------- | -------------------- |
| Sutradhara        | Input (KSML)         |
| DGIC              | Reasoning            |
| PDE               | Recommendation       |
| RAJYA             | Validation Authority |
| Sarathi           | Token Enforcement    |
| Core              | Execution Engine     |
| Integration Layer | Orchestration        |

---

## 🔁 Execution Flow

1. Validate contract
2. Call DGIC → generate reasoning
3. Call PDE → generate recommendation
4. Call RAJYA → validation decision
5. If REJECT → stop execution
6. If APPROVED → generate Sarathi token
7. Execute Core
8. Emit telemetry
9. Return final response

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
* Any violation → HARD FAIL

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
│   └── REVIEW_PACKET.md
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

## ✅ Sample Outputs

### ✔ Approved Case

* Full pipeline executed
* Token generated
* Core execution completed

### ❌ Reject Case

* Stopped at RAJYA
* No token generated
* No Core execution

---

## 📊 Observability

* Contract validation logs at each step
* execution_id trace continuity
* Progressive state visibility
* Clear execution flow logs

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
* No execution without approval
* No execution without token
* Immutable data pipeline

---

## 🔧 Technologies Used

* Python 3
* JSON-based contract system
* Modular orchestration design

---

## 📌 Status

✅ Fully functional
✅ Tested (Approved + Reject flows)
✅ Contract enforced
✅ Integration-ready

---

## 📎 Author

**Akanksha Parab**
Sovereign Core Integration Layer

---

## 📜 License

This project is intended for internal system integration and evaluation.

---
