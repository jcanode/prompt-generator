import anthropic
from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)
OLLAMA_API_URL = "http://localhost:11434/api/generate" # # Update this if your Ollama API is hosted elsewhere

API_KEY = os.environ.get('ANTHROPIC_API_KEY')
client = anthropic.Anthropic(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_prompt', methods=['POST'])
def generate_prompt():
    data = request.get_json()
    if not data or 'task_description' not in data or 'model' not in data:
        return jsonify({"error": "Missing task description or model selection"}), 400

    task_description = data['task_description']
    selected_model = data['model']

    try:
        if selected_model == 'anthropic':
            message = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": f""""Given the following task description, create a high-quality, detailed prompt that will guide an AI to produce excellent results. The prompt should:

                    1. Clearly define the task and its objectives
                    2. Specify the desired format, style, or structure of the output
                    3. Include any relevant context or background information
                    4. Highlight any specific requirements or constraints
                    5. Encourage creativity and thoroughness where appropriate
                    6. Ask for examples or explanations if they would be helpful

                    Task description: {task_description}

                    Based on this task, generate a comprehensive prompt that will elicit the best possible response from an AI system"""}
                ]
            )
            generated_prompt = message.content[0].text
        elif selected_model == 'local':
            # Generate prompt using Ollama API
            ollama_response = requests.post(OLLAMA_API_URL, json={
                "model": "llama3",  # You can change this to any model you have in Ollama
                "prompt": f"""Given the following task description, create a high-quality, detailed prompt that will guide an AI to produce excellent results. The prompt should:

                1. Clearly define the task and its objectives
                2. Specify the desired format, style, or structure of the output
                3. Include any relevant context or background information
                4. Highlight any specific requirements or constraints
                5. Encourage creativity and thoroughness where appropriate
                6. Ask for examples or explanations if they would be helpful

                Task description: {task_description}

                Based on this task, generate a comprehensive prompt that will elicit the best possible response from an AI system""",
                "stream": False
            })
            ollama_response.raise_for_status()
            generated_prompt = ollama_response.json()['response']
        else:
            return jsonify({"error": "Invalid model selection"}), 400

        return jsonify({"prompt": generated_prompt})
    except Exception as e:
        return jsonify({"error": f"Failed to generate prompt: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
