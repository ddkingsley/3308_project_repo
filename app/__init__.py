import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='test', DATABASE=os.path.join(app.instance_path, 'kismet.sqlite'))

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import routes
    app.register_blueprint(routes.bp)
    app.add_url_rule('/', endpoint='index')

    return app