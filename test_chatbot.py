"""
test_chatbot.py

A simple automated verification script to test key units of the Rule-Based AI Chatbot.
Tests sanitization, token intent matching, custom commands, dynamic triggers, and fallback mechanisms.
"""

import sys
import utils
import responses

def run_tests() -> bool:
    print("==================================================")
    print("         RUNNING AUTOMATED UNIT TESTS             ")
    print("==================================================")
    
    passed_tests = 0
    total_tests = 0

    # Helper function to print test results
    def assert_test(name: str, condition: bool) -> None:
        nonlocal passed_tests, total_tests
        total_tests += 1
        if condition:
            print(f"[PASSED] - {name}")
            passed_tests += 1
        else:
            print(f"[FAILED] - {name}")

    # 1. Test Input Sanitization
    print("\n--- Testing: utils.sanitize_input ---")
    assert_test("Trims whitespaces", utils.sanitize_input("  hello   ") == "hello")
    assert_test("Converts to lowercase", utils.sanitize_input("HeLLo") == "hello")
    assert_test("Handles mixed capitalization and padding", utils.sanitize_input("  AbOuT  ") == "about")
    assert_test("Handles empty inputs", utils.sanitize_input("") == "")
    assert_test("Handles None input gracefully", utils.sanitize_input(None) == "")

    # 2. Test Time Formatting Utility
    print("\n--- Testing: utils.get_timestamp ---")
    timestamp = utils.get_timestamp()
    assert_test("Generates HH:MM:SS string", len(timestamp) == 8 and timestamp[2] == ":" and timestamp[5] == ":")

    # 3. Test Intent Matching in responses.py
    print("\n--- Testing: responses.get_response ---")
    
    # Greetings intent
    greetings_res1 = responses.get_response("hello")
    greetings_res2 = responses.get_response("hi")
    greetings_valid = any(res in responses.INTENTS["greetings"]["responses"] for res in [greetings_res1, greetings_res2])
    assert_test("Matches greeting keywords", greetings_valid)

    # Substring / Token matching verification
    about_res = responses.get_response("tell me about the bot")
    about_valid = about_res in responses.INTENTS["about"]["responses"]
    assert_test("Matches 'about' inside a full sentence prompt", about_valid)

    creator_res = responses.get_response("who made you?")
    creator_valid = creator_res in responses.INTENTS["creator"]["responses"]
    assert_test("Matches creator question with punctuation", creator_valid)

    # Dynamic time intent
    time_res = responses.get_response("what time is it")
    assert_test("Dynamically calculates and prints system time", "The current system time is" in time_res)

    # Fallback checking
    fallback_res = responses.get_response("what is the chemical symbol for gold")
    fallback_valid = fallback_res in responses.FALLBACK_RESPONSES
    assert_test("Triggers custom random fallback for unknown inputs", fallback_valid)

    # Empty prompt fallback
    empty_res = responses.get_response("")
    assert_test("Handles empty inputs in response engine", "didn't say anything" in empty_res)

    print("\n==================================================")
    print(f"Test Results: {passed_tests} / {total_tests} tests passed.")
    print("==================================================")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
