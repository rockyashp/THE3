from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My Flask App</h1>
    <p>This is my first Flask web page.</p>
    """

@app.route('/about')
def about():
    return "<h2>About Page</h2><p>Learning Flask is fun!</p>"

if __name__ == '__main__':
    app.run(debug=True)