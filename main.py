"""
main.py

The main runtime executable for the Rule-Based AI Chatbot.
Orchestrates the main conversation loop, input capturing, sanitization, and output formatting.
Designed with proper separation of concerns by delegating parsing and utilities.
"""

import sys
import utils
import responses

def main() -> None:
    # Clear the terminal screen and present the professional banner
    utils.clear_screen()
    utils.print_banner()
    
    print(utils.format_bot_response("Online and ready. Let's talk!"))
    print("-" * 77)

    # Main infinite conversation loop
    while True:
        try:
            # Generate the dynamic prompt with timestamp
            user_prompt = utils.format_user_prefix()
            
            # Capture user input
            raw_input = input(user_prompt)
            
            # 1. Sanitize the input
            sanitized_input = utils.sanitize_input(raw_input)
            
            # 2. Check for exit commands immediately to exit cleanly
            if sanitized_input in ["exit", "quit", "bye", "goodbye"]:
                # Fetch a friendly deterministic farewell response
                farewell = responses.get_response("bye")
                print(utils.format_bot_response(farewell))
                print(f"\n{utils.COLOR_GREEN}{utils.COLOR_BOLD}[System: Chatbot session closed successfully.]{utils.COLOR_RESET}\n")
                break
                
            # 3. Handle extra system-level utility commands
            if sanitized_input == "clear":
                utils.clear_screen()
                utils.print_banner()
                print(utils.format_bot_response("Console cleared! Ask me anything."))
                print("-" * 77)
                continue
                
            if sanitized_input == "version":
                version_info = (
                    f"Rule-Based AI Chatbot [Version 1.0.0]\n"
                    f"  Developed during the AI Engineering Internship.\n"
                    f"  Built using native Python with deterministic intent routing."
                )
                print(utils.format_bot_response(version_info))
                print("-" * 77)
                continue

            # If user pressed enter without typing anything, skip matching
            if not sanitized_input:
                print(utils.format_bot_response("I see you pressed Enter! Tell me what's on your mind, or type 'help'."))
                print("-" * 77)
                continue

            # 4. Process and match intents via the response engine
            bot_reply = responses.get_response(sanitized_input)
            
            # 5. Format and display the chatbot response
            print(utils.format_bot_response(bot_reply))
            print("-" * 77)
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print(f"\n\n{utils.COLOR_RED}{utils.COLOR_BOLD}[System: Session interrupted via KeyboardInterrupt.]{utils.COLOR_RESET}")
            farewell = responses.get_response("bye")
            print(utils.format_bot_response(farewell))
            print()
            sys.exit(0)
            
        except Exception as e:
            # Gracefully handle unexpected runtime issues
            error_message = f"An unexpected system exception occurred: {str(e)}"
            print(utils.format_bot_response(error_message))
            print("-" * 77)

if __name__ == "__main__":
    main()
