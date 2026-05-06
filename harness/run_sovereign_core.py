import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from entry.sovereign_core_entry import invoke_sovereign_core
import json

# -------- APPROVED CASE --------
request_approved = {
    "execution_id": "exec_001",
    "ksml_input": {
        "query": "normal case"
    }
}

# -------- REJECT CASE --------
request_reject = {
    "execution_id": "exec_002",
    "ksml_input": {
        "query": "force reject"
    }
}

# Modify RAJYA behavior dynamically (simple trick)
from entry import sovereign_core_entry

def custom_rajya(request):
    if request["execution_id"] == "exec_002":
        return {"status": "REJECT"}
    return {"status": "APPROVED"}

sovereign_core_entry.call_rajya = custom_rajya


# -------- RUN BOTH --------
print("\n===== APPROVED CASE =====")
response1 = invoke_sovereign_core(request_approved)
print(json.dumps(response1, indent=2))

print("\n===== REJECT CASE =====")
response2 = invoke_sovereign_core(request_reject)
print(json.dumps(response2, indent=2))


# Save logs
with open("logs/execution_logs.json", "w") as f:
    json.dump({
        "approved_case": response1,
        "reject_case": response2
    }, f, indent=2)
