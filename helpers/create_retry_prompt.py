def create_retry_prompt(
        original_prompt, original_response, error_message
):
    """Define a function to create a retry prompt with error feedback"""
    retry_prompt = f"""
        This is a request to fix an error in the structure of an llm_response.
        Here is the original request:
        <original_prompt>
        {original_prompt}
        </original_prompt>

        Here is the original llm_response:
        <llm_response>
        {original_response}
        </llm_response>

        This response generated an error: 
        <error_message>
        {error_message}
        </error_message>

        Compare the error message and the llm_response and identify what 
        needs to be fixed or removed
        in the llm_response to resolve this error. 

        Respond ONLY with valid JSON. Do not include any explanations or 
        other text or formatting before or after the JSON string.
    """
    return retry_prompt
