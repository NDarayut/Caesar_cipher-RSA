from flask import Flask, request, render_template
from caesar_cipher_improved import caesar_cipher_encrypt, caesar_cipher_decrypt
from rsa import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        case_sensitive = 'case_sensitive' in request.form
        foreign_char = 'foreign_char' in request.form
        action = request.form['action']
        if(action == 'encrypt'):
            result = caesar_cipher_encrypt(text, shift, case_sensitive, foreign_char)
        else:
            result = caesar_cipher_decrypt(text, shift, case_sensitive, foreign_char)

        return render_template('index.html', result=result, text=text, shift=shift, action=action)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

