# import aplikasi flask, os, flash, jsonify, redirect, dan render_template untuk dipakai di web kita
import os

#import SQL utk akses database
from cs50 import
#import flash utk notifikasi pada web
#import jsonify utk memformat data
#import redirect dan render_template untuk berpindah halaman web
   

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route('/login')
def login():
    return 'halaman login'
