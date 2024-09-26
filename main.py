from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load the OpenAI API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__, template_folder='templates')

# Route to render the front end (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Handle POST request from the front end to get a response from GPT-4
@app.route('/ask', methods=['POST'])
def ask_gpt():
    data = request.json
    question = data.get('question')

    if question:
        # Use the OpenAI client to generate a response
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a friendly and knowledgeable visa assistant representing iVisa. Begin by warmly greeting the user: 'Hello, I’m your visa assistant from iVisa. How can I assist you today?' Provide clear, concise answers to their visa-related inquiries. At the end of each response, include: 'For further assistance, please contact one of our experts at iVisa by calling +1 (510)-288-5920.'"},
                {"role": "user", "content": question}
            ],
            max_tokens=500,
            temperature=0.2
        )

        # Fetch the assistant's reply from the response
        answer = response.choices[0].message.content.strip()

        return jsonify({"response": answer})  # Returning JSON

    return jsonify({"error": "No question provided."}), 400

if __name__ == "__main__":
    app.run(debug=True)
