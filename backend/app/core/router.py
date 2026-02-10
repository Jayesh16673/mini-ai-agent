from app.utils.parser import (
    extract_math,
    extract_memory_save,
    extract_memory_read
)


def route_prompt(prompt: str):
    p = prompt.lower()

    if "remember" in p:
        key, value = extract_memory_save(prompt)
        return "memory_save", key, value

    if "what is my" in p:
        key = extract_memory_read(prompt)
        return "memory_read", key, None

    if "what is" in p:
        expr = extract_math(prompt)
        return "calculator", expr, None

    return None, None, None
