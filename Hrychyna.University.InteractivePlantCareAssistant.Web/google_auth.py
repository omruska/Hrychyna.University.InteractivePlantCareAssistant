from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
import requests

app = Flask(__name__)
app.secret_key = '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'

google_client_id = '552965535697-9okr222f94jj65cka12e9e39i3c79sjf.apps.googleusercontent.com'
google_client_secret = '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'
google_redirect_uri = 'https://localhost:7222/'

oauth = OAuth(app)


def get_google_oauth_token():
    return session.get('google_token')


@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        return jsonify({'data': me.data})
    return 'Hello! Log in with your Google account: <a href="/login">Log in</a>'


@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/login/authorized')
def authorized():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Login failed.'

    session['google_token'] = (response['access_token'], '')
    me = google.get('userinfo')
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))


google = oauth.remote_app(
    'google',
    consumer_key=google_client_id,
    consumer_secret=google_client_secret,
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    tokengetter=get_google_oauth_token  # Додано tokengetter тут
)


def get_google_oauth_token():
    return session.get('google_token')


if __name__ == '__main__':
    app.run(debug=True)
