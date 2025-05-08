from flask import Flask, render_template, request, jsonify
from core import reference

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/doc')
def document():
    return render_template('document.html')


@app.route('/generate_reference', methods=['POST'])
def generate_reference():
    input_text = request.json.get('inputText')
    harvard_reference = reference(input_text)
    harvard_reference = harvard_reference.replace('\033[3m', '<i>')
    harvard_reference = harvard_reference.replace('\033[0m', '</i>')
    return jsonify({'harvardReference': harvard_reference})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
