from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysql/mydatabase'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        new_message = Message(content=content)
        db.session.add(new_message)
        db.session.commit()
    messages = Message.query.all()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

