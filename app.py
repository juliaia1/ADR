from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})


@app.route('/mojastrona')
def moje_api():
    return jsonify({"message": "Witaj w moim api!"})


@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    return "Hello!"


@app.route('/api/v1/predict')
def predict():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    if num1 and num2:
        try:
            num1 = float(num1)
            num2 = float(num2)
            if num1 + num2 > 5.8:
                return jsonify({"result": 1})
            return jsonify({"result": 0})
        except ValueError:
            return jsonify({"error": "Invalid input"}), 400
    return jsonify({"error": "Missing parameters"}), 400



if __name__ == '__main__':
    app.run()



## example of test
# def test_example():
#     response = requests.get('http://127.0.0.1:5000')
#     print(response.status_code)  # Powinno zwrócić "Hello World!"