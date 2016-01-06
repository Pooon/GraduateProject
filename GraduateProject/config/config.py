import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-what-it-is'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:111111@localhost/project'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    @staticmethod
    def init_app(app):
        pass

