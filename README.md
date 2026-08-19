# Pydantic Validation for LLM

A small study project exploring how to validate structured LLM outputs using [Pydantic](https://docs.pydantic.dev/).

## What it does

- Sends a user query to an LLM and asks it to return structured JSON.
- Validates the LLM's JSON response against a Pydantic model (`CustomerQuery`, which extends `UserInput`).
- If validation fails, automatically builds a retry prompt that includes the original response and the validation error, and asks the LLM to fix it.
- Repeats this validate → retry loop up to a configurable number of attempts until the response matches the expected schema, or gives up and returns the last error.

## Structure

- `main.py` — entrypoint: runs the example flow end to end.
- `app/config/` — settings loaded from environment variables (`.env`).
- `app/clients/` — OpenAI-compatible clients (raw and `instructor`-wrapped).
- `app/models/` — Pydantic models defining the expected data shapes (`UserInput`, `CustomerQuery`, `SupportTicket`, tool argument schemas).
- `app/prompts/` — prompt templates, built as functions so the LLM-facing text lives in one place.
- `app/data/` — in-memory database simulation (`faq_db`, `order_db`).
- `app/tools/` — tool implementations, their JSON schema definitions, and the dispatcher that routes tool calls.
- `app/services/` — orchestration: input validation, customer query generation, tool-calling decision, support ticket generation.
- `app/examples/` — sample user input payloads used by `main.py`.
