# Execution Output

This document contains the actual execution logs of the Sovereign Core Execution Layer, demonstrating both Approved and Reject flows.

---

## ✅ Approved Case

```json
===== APPROVED CASE =====

Starting Sovereign Core Execution
Validating execution contract...
Contract validated successfully

Calling DGIC...
execution_id maintained: exec_001
Current state after DGIC:
{
  "execution_id": "exec_001",
  "ksml_input": {
    "query": "normal case"
  },
  "dgic_output": {
    "analysis": "risk detected"
  }
}

Validating execution contract...
Contract validated successfully

Calling PDE...
execution_id maintained: exec_001
Current state after PDE:
{
  "execution_id": "exec_001",
  "ksml_input": {
    "query": "normal case"
  },
  "dgic_output": {
    "analysis": "risk detected"
  },
  "pde_output": {
    "recommendation": "monitor closely"
  }
}

Validating execution contract...
Contract validated successfully

Calling RAJYA...
execution_id maintained: exec_001
Current state after RAJYA:
{
  "execution_id": "exec_001",
  "ksml_input": {
    "query": "normal case"
  },
  "dgic_output": {
    "analysis": "risk detected"
  },
  "pde_output": {
    "recommendation": "monitor closely"
  },
  "rajya_verdict": {
    "status": "APPROVED"
  }
}

Validating execution contract...
Contract validated successfully

Generating token...
execution_id maintained: exec_001

Validating execution contract...
Contract validated successfully

Executing Core...
execution_id maintained: exec_001

Emitting telemetry...

Execution Completed

{
  "execution_id": "exec_001",
  "ksml_input": {
    "query": "normal case"
  },
  "dgic_output": {
    "analysis": "risk detected"
  },
  "pde_output": {
    "recommendation": "monitor closely"
  },
  "rajya_verdict": {
    "status": "APPROVED"
  },
  "sarathi_token": "secure_token_123",
  "enforcement_result": {
    "result": "execution successful"
  }
}
```

---

## ❌ Reject Case

```json
===== REJECT CASE =====

Starting Sovereign Core Execution
Validating execution contract...
Contract validated successfully

Calling DGIC...
execution_id maintained: exec_002
Current state after DGIC:
{
  "execution_id": "exec_002",
  "ksml_input": {
    "query": "force reject"
  },
  "dgic_output": {
    "analysis": "risk detected"
  }
}

Validating execution contract...
Contract validated successfully

Calling PDE...
execution_id maintained: exec_002
Current state after PDE:
{
  "execution_id": "exec_002",
  "ksml_input": {
    "query": "force reject"
  },
  "dgic_output": {
    "analysis": "risk detected"
  },
  "pde_output": {
    "recommendation": "monitor closely"
  }
}

Validating execution contract...
Contract validated successfully

Calling RAJYA...
execution_id maintained: exec_002
Current state after RAJYA:
{
  "execution_id": "exec_002",
  "ksml_input": {
    "query": "force reject"
  },
  "dgic_output": {
    "analysis": "risk detected"
  },
  "pde_output": {
    "recommendation": "monitor closely"
  },
  "rajya_verdict": {
    "status": "REJECT"
  }
}

Validating execution contract...
Contract validated successfully

Rejected by RAJYA

Emitting telemetry...
```

---

## 📌 Summary

* Approved flow executes full pipeline (DGIC → PDE → RAJYA → Sarathi → Core)
* Reject flow stops at RAJYA
* execution_id is preserved across all layers
* Contract validation enforced at every stage
* Telemetry emitted in both scenarios

---
