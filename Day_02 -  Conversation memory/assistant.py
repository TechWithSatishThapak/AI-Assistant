import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load configuration
load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)
MODEL_NAME = os.getenv("MODEL")


def print_banner():
    """Displays the welcome banner and instructions."""
    print("\n" + "=" * 45)
    print("              My AI Assistant")
    print("   Type 'quit' to exit | 'clear' to reset")
    print("=" * 45)


def show_status(text: str):
    """Displays a temporary status message on the current line."""
    sys.stdout.write(f"\nAI  : {text}")
    sys.stdout.flush()


def clear_status():
    """Clears the temporary status message."""
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()


def main():
    print_banner()

    # Optional: Give the AI a starting personality or role
    messages = [
        {"role": "system", "content": "You are a helpful and concise AI assistant."}
    ]

    while True:
        user_input = input("\nYou : ").strip()

        # 1. Ignore accidental empty presses
        if not user_input:
            continue

        # 2. Check for exit commands BEFORE saving to history
        if user_input.lower() in {"quit", "exit"}:
            print("\nAI  : Goodbye! Have a great day.\n")
            break

        # 3. Allow clearing conversation memory mid-chat
        if user_input.lower() == "clear":
            messages = [messages[0]]
            print("\nAI  : Memory cleared! Starting a fresh conversation.")
            print("-" * 45)
            continue

        # Save the user's message to history
        messages.append({"role": "user", "content": user_input})

        show_status("Thinking...")

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
            )

            ai_reply = response.choices[0].message.content
            clear_status()

            print(f"AI  : {ai_reply}")
            print("-" * 45)

            # Save the AI's reply to history
            messages.append({"role": "assistant", "content": ai_reply})

        except Exception as error:
            clear_status()
            # Remove the failed user message so history stays clean
            messages.pop()
            print(f"AI  : Sorry, an error occurred ({error})")


if __name__ == "__main__":
    main()
