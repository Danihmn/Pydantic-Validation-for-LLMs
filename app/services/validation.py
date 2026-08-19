from app.models.user_input import UserInput


def validate_user_input(user_json: str):
    """Validate user input from a JSON string and return a UserInput
    instance if valid."""
    try:
        user_input = (
            UserInput.model_validate_json(user_json)
        )
        print("user input validated...")
        return user_input
    except Exception as e:
        print(f" Unexpected error: {e}")
        return None
