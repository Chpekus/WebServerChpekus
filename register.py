from flask import Flask, session, redirect, url_for, request


def login():
    session.permanent = True  # Включаем постоянные сессии
    session['username'] = request.form['username']
    return redirect(url_for('index'))



