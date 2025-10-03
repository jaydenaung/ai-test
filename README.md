# AI Test

This repository contains a simple Python application that demonstrates how to interact with OpenAI's API.

## Prerequisites

- Python 3.7 or higher installed on your system.
- An OpenAI API key. You can obtain one from [OpenAI’s platform](https://platform.openai.com/).
- (Optional) Git if you plan to clone the repository from GitHub.

## Setup

1. **Clone the repository** (or download it as a ZIP file):

   ```bash
   git clone https://github.com/jaydenaung/ai-test.git
   cd ai-test
   ```

2. **Create and activate a virtual environment** (recommended):

   On macOS/Linux:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows (Command Prompt):

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install openai
   ```

4. **Set your OpenAI API key**:

   Export your OpenAI API key as an environment variable named `OPENAI_API_KEY`.

   On macOS/Linux:

   ```bash
   export OPENAI_API_KEY=sk-your-key
   ```

   On Windows (Command Prompt):

   ```cmd
   set OPENAI_API_KEY=sk-your-key
   ```

## Running the app

After setting up the environment and dependencies, you can run the app with:

```bash
python app.py
```

The script will send a simple message to OpenAI and print the response to your console.

## Notes

- Make sure you do not commit your API key to version control or share it publicly.
- Feel free to modify `app.py` to experiment with different prompts or models provided by OpenAI.
