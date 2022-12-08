from flask import *
from GrammarParser import *


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    nouns = []
    verbs = []
    refill = ""
    if request.method == "POST":
        refill = request.form['userCase']
        nouns, verbs = parse(refill)
    return render_template('index.html', title='Welcome', nouns=nouns, verbs=verbs, refill=refill)

app.run(host='0.0.0.0', port=81)