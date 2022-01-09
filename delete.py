from main import Post,User,session

# user_to_delete=session.query(User).filter(User.id==1).first()

# session.delete(user_to_delete)
# session.commit()

all_posts=session.query(Post).all()

all_users=session.query(User).all()




print(all_posts)
print(all_users)