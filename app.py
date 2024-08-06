from flask import Flask, render_template, request
import os

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        mode = request.form['mode']
        result = caesar_cipher(text, shift, mode)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
