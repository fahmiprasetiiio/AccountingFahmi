from flask import Flask, request, abort, jsonify
from flask_cors import CORS

import os, json, jwt
import psycopg2, psycopg2.extras

app = Flask(__name__)
cors = CORS(app)
secret_key = 'marinirinfantri'

#membuat Koneksi ke database di postgreSQL
con = psycopg2.connect(database=os.getenv('DATABASE'),user=os.getenv('USER'),password=os.getenv('PASSWORD'),host=os.getenv('HOSTDB'),port=os.getenv('PORTDB'))

# fungsi singUp
@app.route('/signUp', methods=['POST'])
def signUp():
    #mengambil data dari inputan user yang ada di main.js
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    sex = request.json['sex']
    alamat = request.json['alamat']

    cursorSignUp = con.cursor()
    cursorSignUp.execute("Insert into user (nama,email,password,sex,alamat) values(%s,%s,%s,%s,%s,%s)",(nama, email, password, sex, alamat))
    con.commit()

    return "SignUp sukses", 201


if __name__ == '__main__' :
     app.run(debug=True, host=os.getenv('HOST'),port =os.getenv('PORT'))  