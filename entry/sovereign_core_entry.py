from contract.execution_contract_validator import validate_contract
import json


# -------- External System Calls (Mock) --------

def call_dgic(request):
    return {"analysis": "risk detected"}


def call_pde(request):
    return {"recommendation": "monitor closely"}


def call_rajya(request):
    return {"status": "APPROVED"}


def call_sarathi(request):
    return {"token": "secure_token_123"}


def call_core(request):
    return {"result": "execution successful"}


# -------- Main Orchestration Function --------

def invoke_sovereign_core(request):

    print("\n Starting Sovereign Core Execution")

    # -------- CONTRACT VALIDATION --------
    print(" Validating execution contract...")
    validate_contract(request)
    print(" Contract validated successfully")

    # -------- DGIC --------
    print("\n Calling DGIC...")
    request["dgic_output"] = call_dgic(request)

    print(f" execution_id maintained: {request['execution_id']}")
    print(" Current state after DGIC:")
    print(json.dumps(request, indent=2))

    print(" Validating execution contract...")
    validate_contract(request)
    print(" Contract validated successfully")

    # -------- PDE --------
    print("\n Calling PDE...")
    request["pde_output"] = call_pde(request)

    print(f" execution_id maintained: {request['execution_id']}")
    print(" Current state after PDE:")
    print(json.dumps(request, indent=2))

    print(" Validating execution contract...")
    validate_contract(request)
    print(" Contract validated successfully")

    # -------- RAJYA --------
    print("\n Calling RAJYA...")
    request["rajya_verdict"] = call_rajya(request)

    print(f" execution_id maintained: {request['execution_id']}")
    print(" Current state after RAJYA:")
    print(json.dumps(request, indent=2))

    print(" Validating execution contract...")
    validate_contract(request)
    print(" Contract validated successfully")

    # -------- REJECT CHECK --------
    if request["rajya_verdict"]["status"] == "REJECT":
        print("\n Rejected by RAJYA")
        print(" Emitting telemetry...")
        return request

    # -------- SARATHI --------
    print("\n Generating token...")
    request["sarathi_token"] = call_sarathi(request)["token"]

    print(f" execution_id maintained: {request['execution_id']}")

    print(" Validating execution contract...")
    validate_contract(request)
    print(" Contract validated successfully")

    # -------- CORE EXECUTION --------
    print("\n Executing Core...")
    request["enforcement_result"] = call_core(request)

    print(f" execution_id maintained: {request['execution_id']}")

    # -------- TELEMETRY --------
    print(" Emitting telemetry...")

    print("\n Execution Completed")

    return request
