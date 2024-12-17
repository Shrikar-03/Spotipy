'''from flask import Flask, request, redirect, session, url_for, render_template, flash
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session data

# Spotify API credentials
SPOTIPY_CLIENT_ID = '9896c76ec59140e9b8272264405314c8'
SPOTIPY_CLIENT_SECRET = '634c9e958451472a9244b1824c071557'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback'  # Adjust to your deployment URL

# Initialize SpotifyOAuth
sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope="user-library-read")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route("/callback")
def callback():
    try:
        token_info = sp_oauth.get_access_token(request.args.get('code'))
        access_token = token_info['access_token']
        # Store the access token securely in the session for future use.
        session['access_token'] = access_token

        # Use the access token to make Spotify API requests
        sp = Spotify(auth=access_token)
        user_playlists = sp.current_user_playlists()

        # Handle the user's playlists or perform other actions
        # ...

        flash("Authorization successful! You can now use the Spotify API.")
    except Exception as e:
        flash(f"Authorization error: {str(e)}")

    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)'''

from flask import Flask, request, redirect, url_for, render_template, flash, session
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
from models import db, UserToken
import os

app = Flask(__name__)  # Correct the variable name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_tokens.db'
app.secret_key = os.urandom(24)

db.init_app(app)

# Spotify API credentials (replace with your own)
SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000/callback'

sp_oauth = SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope="user-library-read")

@app.route("/")
def index():
    return render_template("index.html")

# The rest of your code remains unchanged
# ...

if __name__ == "__main__":  # Correct the variable name
    with app.app_context():
        db.create_all()
    app.run(debug=True)
