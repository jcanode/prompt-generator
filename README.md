# AI Prompt Generator

This project is a web application that generates high-quality AI prompts based on user-provided task descriptions. It supports using both the Anthropic API and a local Ollama model for prompt generation.

## Features

- User-friendly interface for entering task descriptions
- Option to choose between Anthropic API and local Ollama model
- Pre-defined task examples for quick prompt generation
- Real-time prompt generation with loading indicator
- Copy-to-clipboard functionality for generated prompts

## Prerequisites

- Python 3.7+
- Flask
- Anthropic Python SDK
- Requests library
- Ollama (for local model support)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-prompt-generator.git
   cd ai-prompt-generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Anthropic API key:
   - Create a `.env` file in the project root
   - Add your Anthropic API key: `ANTHROPIC_API_KEY=your_api_key_here`

4. (Optional) Install and set up Ollama for local model support:
   - Follow the instructions at [Ollama's official website](https://ollama.ai/)

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Enter a task description or select a pre-defined example

4. Choose between Anthropic API or Local Model (Ollama)

5. Click "Generate Prompt" to create a high-quality AI prompt

6. Copy the generated prompt to use with your preferred AI model

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
