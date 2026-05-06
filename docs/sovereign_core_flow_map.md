# Sovereign Core Flow Map

## 1. System Overview

The Sovereign Core Execution Layer acts as a unified orchestration layer that connects all subsystems into a single deterministic execution flow.

It does not perform reasoning, validation, or execution itself.
It strictly orchestrates the flow between systems while enforcing contract integrity.

---

## 2. End-to-End Flow

Sutradhara (Input Layer)
↓
DGIC (Reasoning Engine)
↓
PDE (Recommendation Engine)
↓
RAJYA (Validation Authority)
↓
Sarathi (Token Enforcement)
↓
Core (Execution Engine)

---

## 3. Execution Object (execution_request)

A single immutable object flows through all layers.

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

---

## 4. Contract Rules (STRICT)

* The same execution_request object is used across all layers
* execution_id must remain constant throughout the flow
* No field mutation is allowed
* Only new fields can be appended
* Contract validation is performed after every stage
* Any contract violation results in immediate failure

---

## 5. Layer Responsibilities

### Sutradhara

* Accepts structured input (KSML)
* Initializes execution_request

---

### DGIC (Reasoning Layer)

* Input: execution_request (with ksml_input)
* Output: dgic_output
* Role: Generate reasoning/analysis

---

### PDE (Recommendation Layer)

* Input: execution_request + dgic_output
* Output: pde_output
* Role: Provide recommendation
* Constraint: No validation authority

---

### RAJYA (Validation Layer)

* Input: execution_request + prior outputs
* Output: rajya_verdict
* Role: Final decision authority

Decision:

* APPROVED → proceed
* REJECT → stop execution immediately

---

### Sarathi (Token Layer)

* Input: execution_request (approved only)
* Output: sarathi_token
* Role: Generate enforcement token

---

### Core (Execution Layer)

* Input: execution_request + token
* Output: enforcement_result
* Role: Perform final execution

---

## 6. Execution Logic (Deterministic)

1. Validate contract
2. Call DGIC → append dgic_output
3. Validate contract
4. Call PDE → append pde_output
5. Validate contract
6. Call RAJYA → append rajya_verdict
7. Validate contract

IF REJECT:

* Stop execution
* Emit telemetry
* Return response

IF APPROVED:
8. Call Sarathi → append sarathi_token
9. Validate contract
10. Call Core → append enforcement_result
11. Emit telemetry
12. Return final response

---

## 7. Failure Handling

* Missing execution_id → contract failure
* Invalid schema → contract failure
* RAJYA rejection → execution stops
* Token missing → execution not allowed

---

## 8. Observability

* Contract validation logs at each step
* execution_id trace maintained across all layers
* Execution state logged progressively (append-only proof)
* Clear visibility of flow progression

---

## 9. Telemetry

* Telemetry is emitted after:

  * Successful execution
  * RAJYA rejection

* Used for:

  * Monitoring
  * Debugging
  * System health tracking

---

## 10. Key Guarantees

* Deterministic execution
* Single entry point
* No duplicate logic
* Strict contract enforcement
* No execution without approval
* No mutation of data

---

## 11. Integration Mapping

| Layer             | Owner    | Responsibility    |
| ----------------- | -------- | ----------------- |
| DGIC              | Pritesh  | Reasoning         |
| PDE               | System   | Recommendation    |
| RAJYA             | Rajaryan | Validation        |
| Sarathi           | Hemanth  | Token Enforcement |
| Core              | Rajaryan | Execution         |
| Integration Layer | Akanksha | Orchestration     |

---

## 12. Summary

The Sovereign Core Execution Layer transforms fragmented systems into a unified, deterministic, and contract-driven execution pipeline.

It ensures:

* Controlled execution
* Strict validation
* Full observability
* Reliable integration across all layers
