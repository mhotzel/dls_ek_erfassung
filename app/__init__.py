from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = "90873db4c5724cbb6a89164e0af84f3038d587a70b2478d9e162f224a4f3a0dd"

from app import routes
