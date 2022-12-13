from flask import *
from app.GrammarParser import *


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    nouns = []
    verbs = []
    refill = ""
    nothing = ""
    if request.method == "POST":
        refill = request.form['userCase']
        if refill != "":
            nouns, verbs = parse(refill)
            nothing = ""
        else:
            nothing = "Nothing was entered."

    return render_template('index.html', title='Grammatical Parser', refill=refill, nouns=nouns, verbs=verbs, nothing=nothing)

if __name__ == '__main__':
    app.run()