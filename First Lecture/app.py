from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<name>')
def greet(name='Stranger'):
    return render_template('greetings.html', name=name)

@app.route("/order", methods=["GET", "POST"])   
def order():
    if request.method == "POST":
        drink = request.form["drink"]
        print("Drink:", drink)
        return render_template("print.html", drink=drink)
    
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)