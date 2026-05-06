REQUIRED_BASE_FIELDS = ["execution_id", "ksml_input"]

def validate_contract(request):

    # Required fields check
    for field in REQUIRED_BASE_FIELDS:
        if field not in request:
            raise Exception(f"Missing required field: {field}")

    # execution_id checks
    if not isinstance(request["execution_id"], str):
        raise Exception("execution_id must be a string")

    if request["execution_id"] == "":
        raise Exception("execution_id cannot be empty")

    # ksml_input must be dict
    if not isinstance(request["ksml_input"], dict):
        raise Exception("ksml_input must be a dictionary")

    # Optional fields validation (if present)
    if "dgic_output" in request and not isinstance(request["dgic_output"], dict):
        raise Exception("Invalid dgic_output format")

    if "pde_output" in request and not isinstance(request["pde_output"], dict):
        raise Exception("Invalid pde_output format")

    if "rajya_verdict" in request and "status" not in request["rajya_verdict"]:
        raise Exception("Invalid rajya_verdict format")

    return True
