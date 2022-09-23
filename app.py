from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/calculate", methods=['GET','POST'])
def calculate():
    if request.method == 'POST':
        age_control = request.form.get("agecheck")
        age_control = True
        if not age_control:
            return render_template("ageerror.html")
        else:
            try:
                height = float(request.form.get("height"))
                weight = float(request.form.get("weight"))
                result = weight / (height * height)
                return render_template("calculated.html", result=result)
            except ValueError:
                return render_template("valueerror.html")
    else:
        return render_template("calculate.html")

if __name__ == '__main__':
    app.run()
