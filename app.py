import os
import openai


def main():
    # Load API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")
    openai.api_key = api_key

    # Create a test chat completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, OpenAI!"}]
    )
    print(response.choices[0].message["content"])


if __name__ == "__main__":
    main()
