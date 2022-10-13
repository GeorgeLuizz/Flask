from flask import Flask

app = Flask(__name__)

@app.route('/')

def homepage():
    return 'hello world yeah!!'

@app.route('/contatos')

def contato():
    return 'contato: bla bla bla'

if __name__ == "__main__":
    app.run(port=8085, debug=True)

