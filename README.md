# Pydantic Validation for LLM

A small study project exploring how to validate structured LLM outputs using [Pydantic](https://docs.pydantic.dev/).

## What it does

- Sends a user query to an LLM and asks it to return structured JSON.
- Validates the LLM's JSON response against a Pydantic model (`CustomerQuery`, which extends `UserInput`).
- If validation fails, automatically builds a retry prompt that includes the original response and the validation error, and asks the LLM to fix it.
- Repeats this validate → retry loop up to a configurable number of attempts until the response matches the expected schema, or gives up and returns the last error.

## Structure

- `models/` — Pydantic models defining the expected data shapes (`UserInput`, `CustomerQuery`).
- `helpers/` — core logic: calling the LLM, validating its response, and building retry prompts on failure.
- `client.py` / `settings.py` — OpenAI-compatible client configured via environment variables.
- `main.py` — example run: validates a sample user query into a `CustomerQuery`.
