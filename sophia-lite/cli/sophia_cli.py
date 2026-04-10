from backend.llm_bridge import get_llm_response

print("Sophia Lite CLI (type 'exit' to quit)")

while True:
    user = input("You: ")
    if user == "exit":
        break
    print("Sophia:", get_llm_response(user))