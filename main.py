from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():

    lista  = ['Si, sei iscritto' , 'Si, sei un ispettore' , 'iscrizione da rinnovare','la zia ha comprato il carrello', 'il cesare mi sembra ha il mizar ma è meglio chidere alla mamma','siamo a 12']
    prediction = random.choice(lista)

    output = prediction

    return render_template('index.html', prediction_text = output)

@app.route('/results',methods=['POST'])

def results():

    data = request.get_json(force=True)

    lista  = ['Si, sei iscritto' , 'Si, sei un ispettore' , 'iscrizione da rinnovare','la zia ha comprato il carrello','il cesare mi sembra ha il mizar ma è meglio chidere alla mamma','siamo a 12']
    prediction = random.choice(lista)

    output = prediction
    return jsonify(output)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
