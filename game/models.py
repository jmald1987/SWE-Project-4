from game.stuff import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(20), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    score=db.Column(db.Integer)
    highscore=db.Column(db.Integer)
    gamesplayed=db.Column(db.Integer)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.score}','{self.highscore}','{self.gamesplayed}')"
