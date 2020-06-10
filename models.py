#from app import db

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