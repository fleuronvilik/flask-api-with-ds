# Data Structures for Python Developers (w/ Flask)
Watch [course](https://youtu.be/74NW-84BqbA) on @freecodecamp YouTube Channel

## Steps to run locally
1. Create a virtual environment
2. Run the following commands

```
python -m ensurepip --upgrade
python -m pip install -r requirements.txt
python server.py
```

3. Follow http://127.0.0.1:5000/user/3 for example

## Endpoints

<i></i>|User|BlogPost
---|---|---
`GET`|`/user/<user_id>`<br>`/user/ascending_id`<br>`/user/descending_id`|`/blog_post/<blog_post_id>`<br>`/blog_post/numeric_body`
`POST`|`/user`|`/blog_post/<user_id>`
`DELETE`|`/user/<user_id>`|`/blog_post/delete_last_ten`
