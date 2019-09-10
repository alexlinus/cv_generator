import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/cv_generator.db?check_same_thread=False' % APPLICATION_DIR
    DEBUG = True
    SECRET_KEY = 'Gha2sCkx1dggt9iasKXfs!?gk?t1t9'

    # Flask Security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'