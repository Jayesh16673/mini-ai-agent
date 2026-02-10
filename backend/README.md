# Mini AI Agent – Backend

This project is a simple FastAPI backend that acts like a tiny AI assistant.  
Tell it things, ask it about things you told it, or ask it to do a bit of math.

- **Memory Save** — remember stuff you tell it
- **Memory Read** — fetch what you asked it to remember
- **Calculator** — do math for you

---

## 1. How to Set Up the Database and Run the API

### Requirements

- Python 3.10 or above

### Install Dependencies

From the `backend/` folder run:

```powershell
pip install -r requirements.txt
```

### Run the API

From the `backend/` folder run:

```powershell
python -m uvicorn app.main:app --reload
```

If you run from the workspace root, add `--app-dir backend`:

```powershell
python -m uvicorn app.main:app --reload --app-dir backend
```

The server will be at: **http://127.0.0.1:8000**

**Swagger UI:** http://127.0.0.1:8000/docs

### Database

This app uses SQLite. The `memory.db` file is created automatically in the `backend/` folder and the `memory` table is created when the app starts. No manual DB setup is required.

---

## 2. How to Test All Three Tools

Everything goes through one endpoint:

**POST /agent/query**

Send a JSON body like this:

```json
{
  "prompt": "<your prompt>"
}
```

You can try examples in Swagger UI (`/docs`) or use `curl` / Postman.

### Tool 1 — Memory Save

Triggered when the prompt contains the word **"remember"**.

Example request:

```json
{
  "prompt": "Remember my cat's name is Fluffy"
}
```

Example response:

```json
{
  "original_prompt": "Remember my cat's name is Fluffy",
  "chosen_tool": "memory_save",
  "tool_input": "cat's name",
  "response": { "key": "cat's name", "value": "Fluffy" }
}
```

### Tool 2 — Memory Read

Triggered when the prompt contains **"what is my"**.

Example request:

```json
{
  "prompt": "What is my cat's name?"
}
```

Example response (if saved):

```json
{
  "original_prompt": "What is my cat's name?",
  "chosen_tool": "memory_read",
  "tool_input": "cat's name",
  "response": { "key": "cat's name", "value": "Fluffy" }
}
```

If the key doesn't exist the `value` will be `null`.

### Tool 3 — Calculator

Triggered when the prompt contains **"what is"** (and not "what is my"). It extracts the expression and evaluates it.

Example request:

```json
{
  "prompt": "What is 10 + 5?"
}
```

Example response:

```json
{
  "original_prompt": "What is 10 + 5?",
  "chosen_tool": "calculator",
  "tool_input": "10 + 5",
  "response": { "result": 15 }
}
```

### Unsupported Input

If the prompt doesn't match any tool, the API returns an error. Example:

Request:

```json
{
  "prompt": "Tell me a joke"
}
```

Response:

```json
{
  "error": "I do not have a tool for that."
}
```