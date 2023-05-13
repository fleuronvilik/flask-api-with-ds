# Data Structures for Python Developers (w/ Flask)
Watch [course](https://youtu.be/74NW-84BqbA) on @freecodecamp YouTube Channel

## First Steps
1. Create a virtual environment
2. Run the following commands

```
python -m ensurepip --upgrade
python -m pip install -r requirements.txt
```

## Generate Dummy Data
The project includes a script to generate dummy data. Here is how to use it.

1. Start by opening a python console at the root of your project
2. In the console type the following lines

```py
from blog import db
db.create_all()
```

3. There is a sqlite database file named __[sqlitedb.file](https://github.com/fleuronvilik/flask-api-with-ds/blob/8b413cad443bc0396f43690bb4dec6f614f41957/blog/__init__.py#L9)__ in the blog subfolder.
`ls blog` or `ls blog/sqlitedb.file` to check.
4. Run `python generate_dummy_data.py` in the terminal

## Running locally

1. Execute `python server.py` in the terminal
2. View http://127.0.0.1:5000/user/3 (for example) in your browser

## Endpoints

<i></i>|User|BlogPost
---|---|---
`GET`|`/user/<user_id>`<br>`/user/ascending_id`<br>`/user/descending_id`|`/blog_post/<blog_post_id>`<br>`/blog_post/numeric_body`
`POST`|`/user`|`/blog_post/<user_id>`
`DELETE`|`/user/<user_id>`|`/blog_post/delete_last_ten`
