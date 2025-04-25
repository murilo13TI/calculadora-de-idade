from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular_idade_atual', methods=['POST'])
def calcular_idade_atual():

    ano_nascimento = request.form['ano_nascimento']
    idade = 2025 - int(ano_nascimento)

    return render_template('index.html', idade=idade)


if __name__ == '__main__':
    app.run(debug=True)


