from db import db

class Post(db.Model):

    # create columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.Text)
    post_date = db.Column(db.Date)

    # instantiate the object
    def __init__(self, title, desc, p_date):
        self.title = title
        self.desc = desc
        self.post_date = p_date

    # create
    def create(post_dict):
        new_post = Post(
            title = post_dict['title'],
            desc = post_dict['desc'],
            p_date = post_dict['p_date']
        )

        # add to the database and commit the changes
        db.session.add(new_post)
        db.session.commit()
