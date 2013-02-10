from flask import Flask
from flask.ext.babel import Babel
from flask.ext.babel import gettext as _
from flask.ext.heroku import Heroku
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)
babel = Babel(app)
heroku = Heroku(app)


## Models
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('expense_id', db.Integer, db.ForeignKey('expense.id'))
)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    amt = db.Column(db.Float)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    tags = db.relationship('Tag', secondary=tags,
         backref=db.backref('expenses', lazy='dynamic')
    )

    def __str__(self):
        return _('{0}:  {1} ({2})').format(self.date, self.amt, self.currency)


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(10))
    description = db.Column(db.String(50))
    expenses = db.relationship('Expense', backref='currency', lazy='dynamic')


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Unicode, unique=True)

    def __str__(self):
        return self.value


## API routes will be available at /api/<tablename>
manager.create_api(Tag, methods=['GET', 'POST', 'PUT', 'DELETE'])
manager.create_api(Expense, methods=['GET', 'POST', 'PUT', 'DELETE'])


## General routes
@app.route('/')
def app_index():
    return _(u'Welcome.')


@app.route('/about')
def app_about():
    return _(u'More information is forthcoming.')


def setup_db():
    """
    Ensure the database is created.
    """
    db.create_all()


if __name__ == '__main__':
    setup_db()
    app.run()
