# app/routes.py
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from random import randint

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Matheus'}
    posts = [
        {
        'author': {'username': 'Joao'},
        'body': 'Belo dia em Vila Velha!'
        },
        {
        'author': {'username': 'Maria'},
        'body': 'Bora para o cinema hoje?'
        }
    ]
    numero = randint(1, 2)
    if(numero == 1):
        img = 'https://preview.redd.it/tdebr2qaf7ee1.jpeg?width=640&crop=smart&auto=webp&s=1ed7f2e0c74463dd8270f5523e42d7736cf8b627'
    else:
        img = 'https://preview.redd.it/sexaebx7c9ee1.jpeg?width=640&crop=smart&auto=webp&s=2721b0801f7b37bcf1eafd9ca8c92085da27507c'
    
    imgs = [{'a': 'https://s2-ge.glbimg.com/BsRH4rij3O7pZ-gj3JCCLNFcFw0=/0x0:1100x618/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2022/Y/i/dULbPDQDC1fIKuUQQRug/csgo-image.jpg'},
            {'a': 'https://www.baixarcs16agora.com/wp-content/uploads/2020/04/counter-strike-cheats-002.jpg'}]
    return render_template('index.html', title='home', user=user, img=img, posts=posts, imgs = imgs)

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login solicitado pelo usuario {}, Remeber ME = {}".format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)