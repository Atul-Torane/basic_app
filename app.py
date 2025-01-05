from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to My Flask Website</h1><p>This is the home page.</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask website.</p>"

if __name__ == '__main__':
    app.run(debug=True)
