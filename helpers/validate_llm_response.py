from helpers.call_llm import call_llm
from helpers.create_retry_prompt import create_retry_prompt
from helpers.validate_llm_model import validate_with_model


def validate_llm_response(prompt, model_data, n_retry=5):
    # Initial LLM call
    response_content = call_llm(prompt)
    current_prompt = prompt

    # Try to validate with the model
    # attempt: 0=initial, 1=first retry, ...
    for attempt in range(n_retry + 1):
        validated_data, validation_error = validate_with_model(response_content, model_data)

        if validation_error:
            if attempt < n_retry:
                print(f"retry {attempt} of {n_retry} failed, trying again...")
            else:
                print(f"Max retries reached. Last error: {validation_error}")
                return None, (
                    f"Max retries reached. Last error: {validation_error}"
                )

            validation_retry_prompt = create_retry_prompt(current_prompt, response_content, validation_error)
            response_content = call_llm(validation_retry_prompt)
            current_prompt = validation_retry_prompt
            continue

    # If you get here, both parsing and validation succeeded
    return validated_data, None
