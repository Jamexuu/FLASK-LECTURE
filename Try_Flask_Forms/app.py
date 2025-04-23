from flask import Flask, render_template, request, redirect, url_for
from form import RegistrationForm
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '04df204306f918cfb84afeea3ef29fbb'

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        counter = 0
        user_id = f"user{counter}"
        new_data = {
            user_id: {
                'username': form.username.data,
                'email': form.email.data,
                'password': form.password.data
            }
        }

        if os.path.exists('Try_Flask_Forms/user.json'):
            with open('Try_Flask_Forms/user.json', 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {"users": {}}
        else:
            data = {"users": {}}

        data["users"][user_id] = new_data[user_id]

        with open('Try_Flask_Forms/user.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        counter += 1
        return redirect(url_for('success'))

    return render_template('login_form.html', form=form)  

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)