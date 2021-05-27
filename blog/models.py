from blog import db

class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50))
  address = db.Column(db.String(200))
  phone = db.Column(db.String(50))
  posts = db.relationship("BlogPost", cascade="all, delete")

class BlogPost(db.Model):
  __tablename__ = "blog_post"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  body = db.Column(db.String(200))
  date = db.Column(db.Date)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)