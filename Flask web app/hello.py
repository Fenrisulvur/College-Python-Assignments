from random import randint
import os
from flask import Flask, request, render_template, url_for, flash, jsonify, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'thequickbrownfoxjumpedoverthelazydog'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"] or None
        file.save(os.path.join(app.root_path, 'static', 'uploads', secure_filename('uploaded-pic.png')))
        return render_template("home.html")
    else:
        return render_template("home.html")
    

@app.route("/image-upload")
def image_upload():
    return render_template("add-file.html")


@app.route('/rps')
def rps():
    return render_template("rps.html")


@app.route('/rps/request', methods=['GET', 'POST'])
def rps_request():
    if request.method == "POST":
        move = str.lower(request.form.get('move'))
        cpmove = get_cp_move()
        winner = determine_round_outcome(move, cpmove)
        return jsonify({'winner': winner, 'pmove': move, 'cpmove': cpmove})
    else:
        flash("You attempted to access a request page by GET. This is not allowed.")
        return redirect("/rps")

@app.route("/ceaser-cipher")
def ceaser_cipher():
    return render_template("cipher.html")

@app.route('/ceaser-cipher/request', methods=['GET', 'POST'])
def ceaser_cipher_request():
    if request.method == "POST":
        text = str.lower(request.form.get('text'))
        key = int(request.form.get('shift'))
        _method = request.form.get('method')

        if _method == "encrypt":
            cipher = ceaser_cipher()
            encrypted_msg = cipher.encrypt(key, text)
            print("Recieved: ", text, key, encrypted_msg)
            return jsonify({'msg': encrypted_msg})
        else:
            cipher = ceaser_cipher()
            decrypted_msg = cipher.decrypt(key, text)
            print("Recieved: ", text, key, decrypted_msg)
            return jsonify({'msg': decrypted_msg})
    else:
        flash("You attempted to access a request page by GET. This is not allowed.")
        return redirect("/ceaser-cipher")
    

def get_cp_move():
    moves = ["r", "p", "s"]
    cp_move = randint(1, 3)
    translated_move = moves[cp_move-1]
    return translated_move


def determine_round_outcome(p, cp):
    print("Your move - %s, Computer move - %s" % (p, cp))
    if p == "r" and cp == "s" or p == "p" and cp == "r" or p == "s" and cp == "p":
        print("Player wins the round")
        return "player"
    elif cp == "r" and p == "s" or cp == "p" and p == "r" or cp == "s" and p == "p":
        print("Computer wins the round")
        return "cp"
    else:
        print("Stalemate")
        return "stalemate"

class ceaser_cipher:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def init(self):
      print("Ceaser cipher instance created")

    #encrypt a message
    def encrypt(self, key, msg):
      encryption = ""
      for char in msg:
        if char in self.alphabet:
          pos = self.alphabet.find(char)
          encryption += self.alphabet[(pos+key) % len(self.alphabet)]
        else:
          encryption += char
      return encryption

    #decrypt a encrypted message
    def decrypt(self, key, msg):
      decryption = ""
      for char in msg:
        if char in self.alphabet:
          pos = self.alphabet.find(char)
          decryption += self.alphabet[(pos-key) % len(self.alphabet)]
        else:
          decryption += char
      return decryption
