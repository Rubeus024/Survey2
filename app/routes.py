from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm, TextForm
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(form.username.data)
        return redirect('/index')

    return render_template('login.html', title='Sign in', form=form)

@app.route('/text', methods=['GET','POST'])
def text():
    form = TextForm()
    if form.validate_on_submit():
        text = form.text_area.data
        lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','x','r','s','t','u','q','v','w','y','z']
        count = [0]*len(lista)

        for i in text.lower():
            if i in lista:
                count[lista.index(i)]+=1
        result = dict(zip(lista,count))
        flash(result)
        return redirect('/index')

    return render_template('text.html',form=form)


