def extract_math(prompt: str) -> str:
    text = prompt.lower()
    text = text.replace("what is", "")
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("?", "")
    return text.strip()


def extract_memory_save(prompt: str):
    # Remember my cat's name is Fluffy
    text = prompt.lower()
    text = text.replace("remember my", "")
    parts = text.split(" is ")
    return parts[0].strip(), parts[1].strip()


def extract_memory_read(prompt: str):
    # What is my cat's name?
    text = prompt.lower()
    text = text.replace("what is my", "")
    return text.replace("?", "").strip()
