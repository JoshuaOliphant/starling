from flask import Flask, request, render_template
import openai
import os
import logging

openai.api_key = os.environ["OPENAI_API_KEY"]
app = Flask(__name__)


@app.route('/')
def chat_interface():
    return render_template('langui.html')


@app.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    question = request.form.get('question')
    app.logger.info(f"question: {question}")
    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{question}"}],
        temperature=0.8
    )

    # Extract the generated text from the API response
    answer = response.choices[0].message.content
    # Return the user's question and GPT's answer
    return answer


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(debug=True)
