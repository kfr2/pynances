from flask import Flask
from flask.ext.babel import Babel
from flask.ext.babel import gettext as _
from flask.ext.heroku import Heroku


app = Flask(__name__)
babel = Babel(app)
heroku = Heroku(app)


@app.route('/')
def app_index():
    return _(u'Welcome.')


if __name__ == '__main__':
    app.run()
