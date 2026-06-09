print("🤖 Chatbot: Hello! I am your simple AI assistant. Type 'bye' to exit.")
print("_" * 40)
while True:
    user_input = input("You: ").lower().strip()
    if "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hi there! How can I help you today?")
    elif "how are you" in user_input:
        print("🤖 Chatbot: I am just a simple Python script, but I am running perfectly!")
    elif "your name" in user_input:
        print("🤖 Chatbot: My name is AlphaBot, your internship assistant.")
    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Good luck with your studies and preparation! 👋")
        print("_" * 40)
        break  
    else:
        print("🤖 Chatbot: I'm sorry, I am a basic chatbot and didn't quite understand that. Could you try saying 'hello' or 'bye'?")
        
    print("_" * 40)