from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin

#Anyway as login process will interact with DB, it's fair to place login_manager here
from . import login_manager 

#To generate tokens and verify it
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class Role(db.Model):
    __tablename__="roles"
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64),unique=True)
    users=db.relationship("User",backref="role",lazy="dynamic")
    
    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
    password_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<User %r>' % self.username

    # Capsulation: This puts restrictions on accessing variables and methods directly to 
    # prevent accidental modification of data. An object's variable can only be changed by its method.
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter  # User().password = "password"
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #Account confirmation
    confirmed = db.Column(db.Boolean, default=False)
    def generate_confirmation_token(self,expriation=3600):
        s = Serializer(current_app.config["SECRET_KEY"],expriation)
        return s.dumps({"confirm":self.id}).decode('utf-8')
    def confirm(self,token):
        s= Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token.encode("utf-8"))
        except:
            return False
        if data.get("confirm") != self.id:
            return False
        self.confirm= True
        db.session.add(self)
        return True

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))