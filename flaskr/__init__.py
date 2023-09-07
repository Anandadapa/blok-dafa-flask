from flask import Flask
#import aplikasi flask untuk dipakai di web kita

app = Flask(__name__)
#mengatur nama aplikasi

#mengatur uri (universal resource identifier), dan apa yang ditampilkan jika uri tersebut diakses
@app.route('/') # ketika alamat http://127.0.0.1:5000/ dipanggil, maka server akan mengeksekusi fungsi hello()
def hello(): # function dengan nama hello
    return 'hello, world!'

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route('/login')
def login():
    return 'halaman login'
