def filter_response(text):
    blocked = ["illegal", "violence", "harm"]
    if any(w in text.lower() for w in blocked):
        return "I can’t help with that, but I can support you safely."
    return text

def medica_guardrail(text):
    banned = ["diagnosis", "prescribe", "cure"]
    if any(w in text.lower() for w in banned):
        return "This system does not provide medical advice."
    return text