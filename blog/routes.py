from flask import request, jsonify
from blog.models import User, BlogPost
from blog import app, db
from ds import linked_list, binary_search_tree, custom_q, stack

from datetime import datetime
import random

@app.route("/user", methods=["POST"])
def create_user():
  data = request.get_json()
  new_user = User(
    name=data["name"],
    email=data["email"],
    address=data["address"],
    phone=data["phone"],
  )
  db.session.add(new_user)
  db.session.commit()
  return jsonify({"message": "User created"}), 200

@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
  users = User.query.all()
  all_users_ll = linked_list.LinkedList()
  for user in users:
    all_users_ll.add({
      "id": user.id,
      "name": user.name,
      "email": user.email,
      "address": user.address,
      "phone": user.phone,
    })
  return jsonify(all_users_ll.to_list()), 200

@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
  users = User.query.all()
  all_users_ll = linked_list.LinkedList()
  for user in users:
    all_users_ll.append({
      "id": user.id,
      "name": user.name,
      "email": user.email,
      "address": user.address,
      "phone": user.phone,
    })
  return jsonify(all_users_ll.to_list()), 200

@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
  users = User.query.all()
  all_users_ll = linked_list.LinkedList()
  for user in users:
    all_users_ll.add({
      "id": user.id,
      "name": user.name,
      "email": user.email,
      "address": user.address,
      "phone": user.phone,
    })
  user = all_users_ll.get_user_by_id(user_id)
  if user is None:
    return jsonify({"message": "User not found"}), 404
  return jsonify(user), 200

@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
  user = User.query.filter_by(id=user_id).first()
  if user is None:
    return jsonify({"message": "User not found"}), 404
  db.session.delete(user)
  db.session.commit()
  return jsonify({"message": "User deleted"}), 200

@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
  data, now = request.get_json(), datetime.now()

  user = User.query.filter_by(id=user_id).first()
  if user is None:
    return jsonify({"message": "user does not exist"}), 400
  # ht = hash_table.HashTable(10)
  # ht.add_key_value("title", data["title"])
  # ht.add_key_value("body", data["body"])
  # ht.add_key_value("date", now)
  # ht.add_key_value("user_id", user_id)
  # print(ht)

  # print(ht.get_value("title"))
  # print(ht.get_value("body"))
  # print(ht.get_value("date"))
  # print(ht.get_value("user_id"))
  new_blog_post = BlogPost(
    title=data["title"],
    body=data["body"],
    date=now,
    user_id=user_id,
  )
  db.session.add(new_blog_post)
  db.session.commit()
  return jsonify({"message": "new blog post created"}), 200

@app.route("/blog_post/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
  blog_posts = BlogPost.query.all()
  random.shuffle(blog_posts)

  bst = binary_search_tree.BlogPostBST()
  for post in blog_posts:
    bst.insert({
      "id": post.id,
      "title": post.title,
      "body": post.body,
      "date": post.date,
      "user_id": post.user_id
    })

  post = bst.search(blog_post_id)

  if not post:
    return jsonify({"message": "post not found"}), 400
  return jsonify(post)

@app.route('/blog_post/numeric_body', methods=["GET"])
def get_numeric_bodies():
  posts = BlogPost.query.all()

  q, arr = custom_q.Queue(), []
  for post in posts:
    q.enqueue(post)
  for _ in range(len(posts)):
    post = q.dequeue()
    numeric_body = 0
    for char in post.body:
      numeric_body += ord(char)
    arr.append({
      "id": post.id,
      "body": numeric_body,
      "date": post.date,
      "user_id": post.user_id
    })
  return jsonify(arr), 200

@app.route('/blog_post/delete_last_ten', methods=["DELETE"])
def delete_last_ten():
  posts = BlogPost.query.all()
  st = stack.Stack()
  for post in posts:
    st.push(post)
  for _ in range(10):
    post = st.pop()
    db.session.delete(post)
    db.session.commit()
  return jsonify({"message":"success"})