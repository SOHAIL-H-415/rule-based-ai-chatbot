"""
responses.py

Contains the chatbot intents, keywords, and response generation logic.
Utilizes dictionary-based (hashmap) matching to identify user intents deterministically.
Avoids massive nested if-elif-else ladders for clean, scalable, and readable code.
"""

import random
from datetime import datetime

# Define intents with associated keywords and possible responses.
# Some intents can have a list of responses (for variety) or be resolved dynamically.
INTENTS = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "yo", "greetings", "howdy", "hola"],
        "responses": [
            "Hello! I am your rule-based AI assistant. How can I help you today?",
            "Hi there! Great to chat with you. How can I assist?",
            "Hey! Hope you are having a wonderful day. What's on your mind?"
        ]
    },
    "goodbye": {
        "keywords": ["bye", "exit", "quit", "goodbye", "see ya", "farewell"],
        "responses": [
            "Goodbye! Have a productive day ahead.",
            "Farewell! Feel free to chat again whenever you need help.",
            "Bye! Don't hesitate to return if you have more questions."
        ]
    },
    "help": {
        "keywords": ["help", "commands", "menu", "what can you do", "info"],
        "responses": [
            "I'm a rule-based AI chatbot! You can ask me about:\n"
            "  - The project or my creator ('about', 'creator', 'project')\n"
            "  - Internship details ('internship', 'intern')\n"
            "  - Tell you a joke ('joke')\n"
            "  - Check the current time ('time')\n"
            "  - Or just type standard commands like 'clear', 'version', or 'exit'."
        ]
    },
    "about": {
        "keywords": ["about", "purpose", "why do you exist", "explain yourself"],
        "responses": [
            "I am a Rule-Based AI Chatbot, developed to showcase fundamental AI engineering concepts.\n"
            "Unlike ML models, I run on deterministic rules, matching your inputs against a pre-defined lexicon."
        ]
    },
    "creator": {
        "keywords": ["creator", "who made you", "who built you", "developer", "author"],
        "responses": [
            "I was developed as part of an AI Software Engineering Internship project by a motivated student.\n"
            "My goal is to demonstrate clean code, modular architecture, and deterministic input processing!"
        ]
    },
    "internship": {
        "keywords": ["internship", "intern", "work", "role", "experience"],
        "responses": [
            "This project is a key milestone in my AI Software Engineering Internship!\n"
            "It demonstrates standard software engineering practices: modular design, input sanitization, and structured testing."
        ]
    },
    "project info": {
        "keywords": ["project", "code", "architecture", "tech stack", "structure"],
        "responses": [
            "Project Specs:\n"
            "  - Name: Rule-Based AI Chatbot\n"
            "  - Language: Pure Python (Standard Library only)\n"
            "  - Design: Modular Architecture (main.py, responses.py, utils.py)\n"
            "  - Pattern: Tokenized keyword-matching dictionary engine"
        ]
    },
    "jokes": {
        "keywords": ["joke", "jokes", "tell me a joke", "funny", "laugh"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🪲",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
            "Why did the Python programmer get rejected by the compiler? Because he had bad indentation! 🐍",
            "There are 10 types of people in this world: Those who understand binary, and those who don't. 💻"
        ]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "appreciate it", "cool", "awesome", "perfect"],
        "responses": [
            "You are very welcome! Let me know if there's anything else I can do.",
            "Happy to help! Anytime.",
            "My pleasure! Let's keep chatting."
        ]
    },
    "time": {
        "keywords": ["time", "date", "what day is it", "clock"],
        # Marked for dynamic generation in get_response
        "responses": []
    }
}

# Pre-defined fallback responses when no intent is matched.
FALLBACK_RESPONSES = [
    "I'm not quite sure I understand that. Type 'help' to see what I can do!",
    "Hmm, that's outside my rule-based directory. Try asking about the project, internship, or for a joke!",
    "I haven't been programmed with a rule for that specific phrase yet. Could you rephrase?",
    "Interesting! However, my deterministic parser couldn't match that intent. Try typing 'help'."
]

def get_response(sanitized_input: str) -> str:
    """
    Scans the sanitized user input to match keywords defined in the INTENTS dictionary.
    Returns the mapped response (supporting dynamic evaluation for certain intents like 'time').
    If no match is found, returns a random fallback response.
    
    Args:
        sanitized_input (str): The sanitized user input.
        
    Returns:
        str: Mapped or dynamic response.
    """
    if not sanitized_input:
        return "It looks like you didn't say anything! Feel free to type 'help' if you're stuck."

    # 1. Match against intents by searching for keywords in the user's input
    matched_intent = None
    
    # Tokenize input words to avoid false positive substring matches (e.g. "hi" in "this")
    input_tokens = sanitized_input.split()

    for intent, config in INTENTS.items():
        keywords = config["keywords"]
        for keyword in keywords:
            # Check for exact token match or full phrase containment to capture longer phrases
            if keyword in input_tokens or keyword == sanitized_input or (len(keyword.split()) > 1 and keyword in sanitized_input):
                matched_intent = intent
                break
        if matched_intent:
            break

    # 2. Generate response based on matched intent
    if matched_intent == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"The current system time is {current_time} on {current_date}."
        
    elif matched_intent:
        # Select a random response from the matched intent for conversational variety
        return random.choice(INTENTS[matched_intent]["responses"])

    # 3. Fallback to default response if no keywords matched
    return random.choice(FALLBACK_RESPONSES)
