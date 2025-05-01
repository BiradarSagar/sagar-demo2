def chatbot():
    print("Welcome to ShopMate Assistant! 🤖")
    print("Type 'exit' to end the chat.\n")

    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I assist you with?",
        "what is your return policy": "You can return any product within 30 days of delivery.",
        "how do i return a product": "To return a product, go to 'My Orders', select the item and click 'Return'.",
        "what are your working hours": "Our customer service is available 24/7!",
        "where is my order": "Please login to your account and check 'My Orders' for the latest tracking information.",
        "do you ship internationally": "Yes, we ship to over 50 countries. Shipping charges may apply.",
        "thank you": "You're welcome! 😊 Anything else I can help you with?",
        "bye": "Goodbye! Have a great day! 👋"
    }

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Bot: Thanks for chatting with us! 👋")
            break
        found = False
        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                found = True
                break
        if not found:
            print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
chatbot()


#Welcome to ShopMate Assistant! 🤖
#Type 'exit' to end the chat.

#You: hello
#Bot: Hi there! How can I help you today?

#You: what is your return policy
#Bot: You can return any product within 30 days of delivery.

#You: how do i return a product
#Bot: To return a product, go to 'My Orders', select the item and click 'Return'.

#You: what are your working hours
#Bot: Our customer service is available 24/7!

#You: where is my order
#Bot: Please login to your account and check 'My Orders' for the latest tracking information.

#You: do you ship internationally
#Bot: Yes, we ship to over 50 countries. Shipping charges may apply.

#You: thank you
#Bot: You're welcome! 😊 Anything else I can help you with?

#You: bye
#Bot: Goodbye! Have a great day! 👋

#You: exit
#Bot: Thanks for chatting with us! 👋
