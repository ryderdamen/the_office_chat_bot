import os
from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import levenshtein_distance


app = Flask(__name__)
chatbot = ChatBot(
    'Office',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./db.sqlite3',
    statement_comparison_function=levenshtein_distance
)

@app.route('/')
def main():
    return jsonify({
        'instructions': 'Welcome to the Office Chat Bot. To evoke a response, visit the /talk/ URL and provide your input text as an ?input parameter',
        'example': os.path.join(request.base_url, 'talk/?input=Hello Dwight'),
    })

@app.route('/talk/')
def talk():
    """Accepts input text parameter and returns response"""
    input_text = request.args.get('input', None)
    if not input_text:
        return jsonify({
            'error': 'Please provide the `input` parameter with your GET request'
        })
    return jsonify({
        'textResponse': str(chatbot.get_response(input_text))
    })


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
