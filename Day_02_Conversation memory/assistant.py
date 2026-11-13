import os
import re
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


def clean_reply(text: str) -> str:
    """Removes any leftover Qwen <think> blocks and extra blank lines."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()


def main():
    print_banner()

    # Strict prompt tailored for qwen3:1.7b
    system_prompt = {
        "role": "system",
        "content": (
            "Reply ONLY in English. Never use Chinese characters. "
            "Give clear, well-structured answers using bullet points. /no_think"
        ),
    }
    messages = [system_prompt]

    while True:
        try:
            user_input = input("\nYou : ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nAI  : Goodbye! Have a great day.\n")
            break

        # 1. Ignore accidental empty presses
        if not user_input:
            continue

        # 2. Check for exit commands BEFORE saving to history
        if user_input.lower() in {"quit", "exit"}:
            print("\nAI  : Goodbye! Have a great day.\n")
            break

        # 3. Allow clearing conversation memory mid-chat
        if user_input.lower() == "clear":
            messages = [system_prompt]
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
                temperature=0.2,        # Stops random language switching
                top_p=0.85,             # Keeps word choices focused
                frequency_penalty=0.2,  # Prevents repetitive phrasing
            )

            raw_reply = response.choices[0].message.content
            ai_reply = clean_reply(raw_reply)
            clear_status()

            print(f"AI  : {ai_reply}")
            print("-" * 45)

            # Save the cleaned reply to history
            messages.append({"role": "assistant", "content": ai_reply})

        except Exception as error:
            clear_status()
            messages.pop()
            print(f"AI  : Sorry, an error occurred ({error})")


if __name__ == "__main__":
    main()
