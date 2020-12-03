from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
database_name = "casting"
database_path = "postgres://ohogniusfwxuez:24e83d55df6cce70e090bdda34a63ca02b981dbea58d68d600c4bd40964278cb@ec2-34-237-89-96.compute-1.amazonaws.com:5432/d1ria34nuces3q"


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def setup_migrations(app):
    migrate = Migrate(app, db)


def create_and_drop_all():
    # db.drop_all()
    db.create_all()





class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_format(self):
        return({
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        })

    def __repr__(self):
        return f'Actor: {self.id}, {self.name}'


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)
    genre = db.Column(db.String(), nullable=False, default='')
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_format(self):
        return({
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.isoformat(),
            "genre": self.genre
        })

    def __repr__(self):
        return f'Movie:{self.id}, {self.title}'
