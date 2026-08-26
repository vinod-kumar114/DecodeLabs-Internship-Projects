"""
DecodeLabs - Artificial Intelligence Internship
Project 1: Rule-Based AI Chatbot

Goal:
    Create a simple rule-based chatbot that responds to predefined
    user inputs using if-else logic, running in a continuous loop.

Key Requirements met:
    - Handles greetings and exit commands
    - Uses if-else logic for responses
    - Runs in a continuous loop (keeps chatting until user exits)

Author: Vinod
"""

import random


def get_response(user_input):
    """
    Takes the user's message, cleans it up, and returns a rule-based
    response using plain if-else / control-flow logic.
    """
    text = user_input.lower().strip()

    # --- Greetings ---
    if text in ("hi", "hello", "hey", "hii", "helo", "hy"):
        responses = [
            "Hello there! How can I help you today?",
            "Hey! Nice to see you.",
            "Hi! What's on your mind?",
        ]
        return random.choice(responses)

    elif "good morning" in text:
        return "Good morning! Hope you have a great day ahead."

    elif "good night" in text:
        return "Good night! Sleep well."

    # --- How are you ---
    elif "how are you" in text:
        return "I'm just a bunch of if-else statements, but I'm doing great! How about you?"

    # --- Identity questions ---
    elif "your name" in text:
        return "I'm ChatBot, a rule-based AI built for DecodeLabs Project 1."

    elif "who made you" in text or "who created you" in text:
        return "I was built by Vinod as part of the DecodeLabs AI Internship."

    # --- Small talk ---
    elif "how old are you" in text:
        return "I don't have an age, I was just compiled and ran today!"

    elif "thank" in text:
        return "You're welcome!"

    elif "help" in text:
        return "You can say hi, ask my name, ask how I'm doing, or type 'bye' to exit."

    # --- Exit commands ---
    elif text in ("bye", "exit", "quit", "goodbye", "see you"):
        return "EXIT"

    # --- Fallback for anything not covered ---
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can do."


def chatbot():
    """
    Runs the chatbot in a continuous loop until the user
    types an exit command (bye / exit / quit / goodbye).
    """
    print("=" * 50)
    print(" Welcome to ChatBot - DecodeLabs Project 1")
    print(" (Type 'bye' or 'exit' to end the chat)")
    print("=" * 50)

    while True:
        user_input = input("You: ")

        if user_input.strip() == "":
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day. 👋")
            break
        else:
            print("Bot:", response)


if __name__ == "__main__":
    chatbot()
