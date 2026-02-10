from fastapi import APIRouter
from app.schemas.agent import AgentRequest
from app.core.router import route_prompt
from app.tools.memory import tool_save_memory, tool_get_memory
from app.tools.calculator import tool_calculate

router = APIRouter()


@router.post("/agent/query")
def agent_query(req: AgentRequest):
    tool, a, b = route_prompt(req.prompt)

    if tool == "memory_save":
        result = tool_save_memory(a, b)
    elif tool == "memory_read":
        result = tool_get_memory(a)
    elif tool == "calculator":
        result = tool_calculate(a)
    else:
        return {"error": "I do not have a tool for that."}

    return {
        "original_prompt": req.prompt,
        "chosen_tool": tool,
        "tool_input": a,
        "response": result
    }
