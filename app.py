from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:david@localhost:5432/bulletin_board"
db = SQLAlchemy(app)

class Bulletin(db.Model):
    __tablename__ = 'bulletin'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    body = db.Column(db.String())
    published = db.Column(db.String())
    user_id = db.Column(db.Integer)

    def __init__(self, title, body, published, user_id):
        self.title = title
        self.body = body
        self.published = published
        self.user_id = user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'title': self.title,
            'body': self.body,
            'published': self.published
        }

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
        }

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add", methods=["POST"])
def add_bulletin():
    title=request.args.get('title')
    body=request.args.get('body')
    published=request.args.get('published')
    try:
        bulletin=Bulletin(
            title=title,
            body=body,
            published=published,
            user_id=user_id
        )
        db.session.add(bulletin)
        db.session.commit()
        return "Bulletin added. id={}".format(bulletin.id)
    except Exception as e:
	    return(str(e))

@app.route('/bulletins')
def bulletins():
    return render_template('bulletins.html')

@app.route('/new')
def createBulletin():
    return render_template('create.html')

@app.route('/edit')
def editBulletin():
    return render_template('edit.html')

if __name__ == '__main__':
    app.run()
