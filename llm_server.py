from transformers import pipeline
from flask import Flask, request, jsonify

# Initialize LLM pipeline (change model name as needed)
llm_generator = pipeline('text-generation', model='distilgpt2')

# Initialize Flask app
app = Flask(__name__)

# Define endpoint for generating text
@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    response = llm_generator(prompt, max_length=50, num_return_sequences=1)
    return jsonify({'generated_text': response[0]['generated_text']})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
