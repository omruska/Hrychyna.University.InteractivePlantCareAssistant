from flask import Flask, redirect, url_for, session, request, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'af502f438758befee078e896ce8cd11080b45937fd6ed0ce2c31152ebe75a6f1'

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='552965535697-9okr222f94jj65cka12e9e39i3c79sjf.apps.googleusercontent.com',
    client_secret='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',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    client_kwargs={'scope': 'openid profile email'}
)


@app.route('/')
def index():
    if 'google_token' in session:
        user_info = google.get('userinfo')
        return jsonify({'data': user_info.json()})
    return 'Hello! Log in with your Google account: <a href="/login">Log in</a>'


@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    if not token:
        return 'Login failed.'

    session['google_token'] = token
    user_info = google.get('userinfo').json()
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
