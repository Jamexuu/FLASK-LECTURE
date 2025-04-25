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
        path ='Try_Flask_Forms/user.json'

        if os.path.exists(path):
            with open(path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {"users": {}}
        else:
            data = {"users": {}}

       # Generate a unique user ID
        user_id = f"user{len(data['users']) + 1}"

        # Add the new user to the dictionary
        data["users"][user_id] = {
            'username': form.username.data,
            'email': form.email.data,
            'password': form.password.data
        }

        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        
        return redirect(url_for('success'))

    return render_template('login_form.html', form=form)  

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)