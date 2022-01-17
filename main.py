from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), nullable=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for elem in Users.query.all():
            if request.form['user'] == elem.user:
                return render_template('greetings_registered_user.html', user=request.form['user'])
        user = Users(user=request.form['user'])
        db.session.add(user)
        db.session.commit()
        return render_template('greetings.html', user=request.form['user'])
    else:
        return render_template('login.html')


@app.route('/users-list')
def users_list():
    users = Users.query.all()
    return render_template('users_list.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)