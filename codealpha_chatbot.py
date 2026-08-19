import random


def chatbot_response(user_input):
    """
    Generate a response based on the user's message.
    This is a rule-based chatbot, so it responds
    according to predefined keywords.
    """

    # Convert the user's message to lowercase
    message = user_input.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii", "helo"]:
        responses = [
            "Hey! How are you doing?",
            "Hi there! Nice to chat with you.",
            "Hello! How can I help you today?",
            "Hey! What's up?"
        ]
        return random.choice(responses)

    # Asking how the chatbot is doing
    elif "how are you" in message or "how are u" in message:
        responses = [
            "I'm doing great! Thanks for asking.",
            "I'm good! Ready to chat with you.",
            "I'm doing pretty well. How about you?"
        ]
        return random.choice(responses)

    # Asking the chatbot's name
    elif "your name" in message or "who are you" in message:
        return "I'm a simple Python chatbot. You can call me PyBot!"

    # User introduces themselves
    elif "my name is" in message:
        name = message.replace("my name is", "").strip()

        if name:
            return f"Nice to meet you, {name.title()}!"
        else:
            return "Nice to meet you! What's your name?"

    # Asking for help
    elif "help" in message:
        return (
            "Sure! You can say hello, ask me how I am, "
            "tell me your name, ask for the time, or simply chat with me."
        )

    # Asking about Python
    elif "python" in message:
        return (
            "Python is a really useful programming language. "
            "I'm actually built using Python!"
        )

    # Thanking the chatbot
    elif "thank you" in message or "thanks" in message:
        responses = [
            "You're welcome!",
            "No problem! 😊",
            "Anytime!",
            "Glad I could help!"
        ]
        return random.choice(responses)

    # Positive responses
    elif message in ["good", "great", "fine", "awesome", "i am good"]:
        return random.choice([
            "That's great to hear!",
            "Nice! I'm glad you're doing well.",
            "Awesome! Keep that energy going."
        ])

    # Negative responses
    elif message in ["sad", "bad", "not good", "tired"]:
        return random.choice([
            "I'm sorry to hear that. I hope things get better soon.",
            "Sounds like you've had a rough time. Take it easy!",
            "I hope your day gets a little better."
        ])

    # Asking what the chatbot can do
    elif "what can you do" in message:
        return (
            "I'm a basic rule-based chatbot, so I can respond "
            "to common messages and questions using predefined replies."
        )

    # Goodbye
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! It was nice chatting with you. Have a great day! 👋"

    # Default response when the chatbot doesn't understand
    else:
        responses = [
            "Hmm, I'm not sure how to respond to that yet.",
            "Interesting! I'm still learning how to handle that.",
            "I don't quite understand that, but I'm happy to keep chatting.",
            "I'm a simple chatbot, so I don't know how to answer that yet."
        ]
        return random.choice(responses)


def start_chat():
    """
    Start the chatbot conversation.
    """

    print("=" * 45)
    print("        Welcome to PyBot!")
    print("=" * 45)
    print("Hi! I'm PyBot, a simple Python chatbot.")
    print("Type 'bye' whenever you want to leave.")
    print()

    while True:

        # Get input from the user
        user_input = input("You: ").strip()

        # Check if the user entered nothing
        if not user_input:
            print("PyBot: Don't be shy! Say something. ")
            continue

        # Get chatbot response
        response = chatbot_response(user_input)

        print("PyBot:", response)

        # End conversation when user says goodbye
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            break


# Start the chatbot
if __name__ == "__main__":
    start_chat()