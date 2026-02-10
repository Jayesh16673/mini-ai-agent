def tool_calculate(expression: str) -> dict:
    try:
        result = eval(expression)
        return {"result": result}
    except:
        return {"error": "Invalid expression"}
