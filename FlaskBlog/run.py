from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# >>> from flaskblog import create_app
# >>> from flaskblog._init_ import db
# >>> from flaskblog.models import current_app, User, Post
# >>> app = create_app()
# >>> app.app_context().push()
# >>> print (app)

# # Now you can run queries against your database.
# >>> User.query.all()
# >>> Post.query.all()

# To drop all table in db
# db.drop_all()

# To create new table
#db.create_all()
