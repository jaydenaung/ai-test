import os
from openai import OpenAI


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
   l     raise ValueError("Please set the OPENAI_API_KEY environment variable.")

    # Create a client instance using the provided API key
    client = OpenAI(api_key=api_key)

    # Send a test chat completion request
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, OpenAI!"}]
    )

    # Print the assistant's reply from the response
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
