from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

url = " https://api.npoint.io/c790b4d5cab58020d391"
post_response = requests.get(url).json()
post_objects = []
for i in post_response:
    post = Post(i['id'], i['title'], i['subtitle'], i['body'])
    post_objects.append(post)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/post/<int:post_id>')
def post(post_id):
    req_post = None
    for post in post_objects:
        if post.id == post_id:
            req_post = post

    return render_template("post.html", post=req_post)


if __name__ == "__main__":
    app.run(debug=True)
