from model_loader import load_model
from chat_memory import ChatMemory

def main():
    qa = load_model()
    memory = ChatMemory(max_turns=3)

    print("Chatbot: Hello! Ask me anything. Type /exit to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Chatbot: Exiting chatbot. Goodbye!")
            break

        response = qa(user_input, max_new_tokens=50)[0]["generated_text"]
        memory.add_turn(user_input, response)

        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()
