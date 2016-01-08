import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-what-it-is'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:111111@localhost/project?charset=utf8'
    

    @staticmethod
    def init_app(app):
        pass

