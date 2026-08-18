from pydantic import ValidationError


def validate_with_model(llm_response, model_data):
    try:
        validated_data = model_data.model_validate_json(llm_response)
        print(f"Data validated successfully:\n{validated_data.model_dump_json(indent=4)}")
        return validated_data, None
    except ValidationError as e:
        print(f"Error validating data: {e}")
        error_message = f"This response generated a validation error: {e}"
        return None, error_message
