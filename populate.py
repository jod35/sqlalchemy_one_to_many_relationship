from main import Post,User,session


new_user=User(
    username="testuser",
    email="testuser@gmail.com"
)

session.add(new_user)
session.commit()


posts=[
    {
        "title":"Learn Django",
        "content":"Lorem ipsum"
    },
      {
        "title":"Learn Java",
        "content":"Lorem ipsum"
    },
      {
        "title":"Learn Javascript",
        "content":"Lorem ipsum"
    },
      {
        "title":"Learn HTML",
        "content":"Lorem ipsum"
    },
      {
        "title":"Learn css",
        "content":"Lorem ipsum"
    },

]

user=session.query(User).filter(User.id==1).first()


# for post in posts:
#     new_post=Post(
#         title=post['title'],
#         content=post['content'],
#         author=user
#     )

#     session.add(new_post)
#     session.commit()

#     print(f"Post cREATED {post['title']}")


post=session.query(Post).filter(Post.id==1).first()
print(post.author)
print(user.posts)