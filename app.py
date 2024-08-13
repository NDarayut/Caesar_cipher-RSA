from flask import Flask, request, render_template
from caesar_cipher_improved import caesar_cipher_encrypt, caesar_cipher_decrypt
from rsa import key_generation, rsa_encryption, rsa_decryption, is_prime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    text = None
    shift = None
    action = None
    algorithm = None
    prime_p = None
    prime_q = None
    d = None
    n = None
    error_message = None

    if request.method == 'POST':
        print(request.form)  # Add this line to see the form data
        try:
            text = request.form['text']
            action = request.form['action']
            algorithm = request.form['algorithm']

            if algorithm == 'caesar':
                shift = int(request.form['shift'])
                case_sensitive = 'case_sensitive' in request.form
                foreign_char = 'foreign_char' in request.form

                if action == 'encrypt':
                    result = caesar_cipher_encrypt(text, shift, case_sensitive, foreign_char)
                else:
                    result = caesar_cipher_decrypt(text, shift, case_sensitive, foreign_char)
            
            elif algorithm == 'rsa':
                if action == 'encrypt':
                    prime_p = int(request.form['prime_p'])
                    prime_q = int(request.form['prime_q'])
                    case_sensitive = 'case_sensitive' in request.form
                    foreign_char = 'foreign_char' in request.form

                    if not is_prime(prime_p) or not is_prime(prime_q):
                        raise ValueError("Both p and q must be prime numbers.")
                    elif prime_p == prime_q:
                        raise ValueError("Both p and q must have different prime numbers.")

                    public_key, private_key = key_generation(prime_p, prime_q)
                    d, n = private_key
                    if action == 'encrypt':
                        cipher_list = rsa_encryption(public_key, text, foreign_char, case_sensitive)
                        result = ' '.join(map(str, cipher_list))
                
                else:
                    d = int(request.form['d'])
                    n = int(request.form['n'])
                    cipher_text = [i for i in text.split()]
                    decrypted_list = rsa_decryption((d, n), cipher_text)
                    result = ''.join(decrypted_list)
        
        except Exception as e:
            error_message = str(e)
       
        return render_template('index.html', result=result, text=text, shift=shift,
                            action=action, algorithm=algorithm, prime_p=prime_p, prime_q=prime_q,
                            d=d, n=n, error_message=error_message)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
