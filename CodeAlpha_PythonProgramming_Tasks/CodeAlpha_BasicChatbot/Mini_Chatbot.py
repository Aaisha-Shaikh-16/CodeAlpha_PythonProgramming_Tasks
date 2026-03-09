# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 12:12:10 2026
@author: Shaikh Aaisha
"""
'''
TASK 3: Basic Chatbot
Goal: 
    Build a simple rule-based chatbot.
Scope:
    Input from user like: "hello", "how are you", "bye".
    Predefined replies like: "Hi!", "I'm fine, thanks! ", "Goodbye!".
Key Concepts Used: if-elif, functions, loops, input/output.
'''
# For randomized replies
import random  

# Store user memory
username = None

# To generate responses
def chatbot_response(user_input):
    global username  # Allows updating name
    
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        replies = ["Hi there!",
                   "Hello!",
                   "Hey!",
                   "Nice to see you!"]
        return random.choice(replies)

    # Asking name
    elif "my name is" in user_input:
        username = user_input.replace("my name is", "").strip().title()
        return f"Nice to meet you, {username}!"

    # How are you
    elif "how are you" in user_input:
        replies = [
            "I'm doing great!",
            "All good here",
            "I am Fine!",
            "Feeling smart today"
        ]
        return random.choice(replies)

    # Asking chatbot name
    elif "your name" in user_input:
        return "I am your friendly chatbot "

    # Simple emotions detection
    elif any(word in user_input for word in ["sad", "tired", "upset"]):
        replies = [
            "I'm sorry to hear that.",
            "I hope the situation would be better soon."
            "Hope things get better soon!",
            "Want to talk about it?"
        ]
        return random.choice(replies)

    # Thank you
    elif "thank" in user_input:
        replies = ["You're welcome!",
                   "No problem!",
                   "Welcome!",
                   "Anytime!"]
        return random.choice(replies)

    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye"]):
        replies = ["Goodbye!",
                   "See you later!",
                   "Have a good day ahead!",
                   "Bye"]
        return random.choice(replies)

    # Default fallback (mini AI feel)
    else:
        replies = [
            "Interesting... tell me more.",
            "Hmmm",
            "I see!",
            "Can you explain that differently?"
        ]
        return random.choice(replies)


# Chat loop
print("Mini AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower() in ["bye", "goodbye"]:
        break

