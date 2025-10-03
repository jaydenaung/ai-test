import os
from openai import OpenAI



def main():

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)

    # Initialize conversation history with a system prompt
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Type 'exit' or 'quit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Assistant: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        assistant_reply = response.choices[0].message.content.strip()
        print(f"Assistant: {assistant_reply}")
        messages.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()
