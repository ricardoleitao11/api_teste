import flask
from flask import request, jsonify


hoteis = [
    {
        "id":0,
        "nome":"Disney All-Start Sports",
        "categoria":"value"
    },
    {
        "id":1,
        "nome":"Disney All-Start Music",
        "categoria":"value"
    },
    {
        "id":2,
        "nome":"Disney All-Start Movies",
        "categoria":"value"
    }
    ]
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
    return "<h1>API Teste 4ECR</h1><h5>Aula Andre 2020</h5><p>Sistemas Distribuidos e Cloud Computing</p>"


@app.route("/api/v1/hoteis/all", methods=["GET"])
def api_all():
    return jsonify(hoteis)
    

@app.route("/api/v1/resources/hoteis", methods=["GET"])
def api_id():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        return 'Erro: nenhum id foi informado. Por favor, especifique esse dado!'

    resultados= []

    for hotel in hoteis:
        if hotel['id'] == id:
            resultados.append(hotel)
    return jsonify(resultados)




app.run()
























