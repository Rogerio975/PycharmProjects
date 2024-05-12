from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem-vindo ao meu aplicativo Flask!"

@app.route('/hello')
def hello():
    return "Olá, mundo!"

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        try:
            result = int(num1) + int(num2)
            return jsonify({'result': result})
        except ValueError:
            return jsonify({'error': 'Os números fornecidos não são válidos.'}), 400
    else:
        return jsonify({'error': 'Por favor, forneça num1 e num2.'}), 400

if __name__ == '__main__':
    app.run(debug=True)