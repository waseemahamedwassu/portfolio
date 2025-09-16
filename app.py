# portfolio
from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, port=port)
