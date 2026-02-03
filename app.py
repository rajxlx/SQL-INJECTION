from flask import Flask, request, render_template
from vulnerable.vulnerable_login import vulnerable_login
# for secure [from secure.secure_login import secure_login as vulnerable_login]


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = vulnerable_login(
            request.form['username'],
            request.form['password']
        )
        if user:
            return render_template('dashboard.html', user=user)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
