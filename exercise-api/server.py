#write a flask API which can return square of a number 
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/',methods=["GET"])
def home_page():
    message = "Hello , I am learning development of API in GCP "
    response = {'my_response':message}
    return jsonify(response)

@app.route("/calculate/<int:num>",methods=["GET"])
def calculate_square(num):
    response = {'Given number is ':num,
                'Square of number':num**2}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")