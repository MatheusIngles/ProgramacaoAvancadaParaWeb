# app/routes.py
from urllib.parse import urlsplit
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm
from random import randint
import sqlalchemy as sa
from app.models import User, Post
from urllib.parse import urlsplit
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/index')
@login_required

def index():
    user = {'username': 'Matheus'}
    query =  sa.select(Post)
    posts = db.session.scalars(query).all()
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))


    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if  user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')

        flash("Login solicitado pelo usuario {}, Remeber ME = {}".format(form.username.data, form.remember_me.data))
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    posts = [
    {'author': user, 'body': 'Test post #1'},
    {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
