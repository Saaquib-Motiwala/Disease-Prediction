from flask import Flask
from flask import render_template, request
from prediction_model.predictor import predictor

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        symptoms = list(request.form.get("passer").split(","))
        prediction = predictor(symptoms)
        data = {
            "name": name,
            "age": age,
            "gender": gender,
            "symptoms": symptoms,
            "prediction": prediction
        }
        print(data)
        return render_template("results.html", data=data)
    return "Wrong request"


if __name__ == '__main__':
    app.run()
