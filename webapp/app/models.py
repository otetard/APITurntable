# encoding: utf-8

from datetime import datetime
from app.ext.sqlalchemy import db


class Pivot(db.Model):

    __tablename__ = 'pivot'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)
    deleted = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    def producers(self):
        p1 = Producer()
        p1.pivot_id = self.id
        p1.url_path = "jkhjgsqdjhgqjs-qsjdqsd-qksjdqksdkqsdkqsjdkl"
        p1.name = "github"
        return [
            p1
        ]

    def consumers(self):
        c1 = Consumer()
        c1.pivot_id = self.id
        c1.url_path = "jkhjgsqdjhgqjs-qsjdqsd-qksjdqksdkqsdkqsjdkl"
        c1.name = "client"
        return [
            c1
        ]
    

class Consumer(db.Model):

    __tablename__ = 'consumer'

    id = db.Column(db.Integer, primary_key=True)
    pivot_id = db.Column(db.Integer(), nullable=False)
    url_path = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    @property
    def url(self):
        return 'apipivots.io/ci/{}'.format(self.url_path)

class Producer(db.Model):

    __tablename__ = 'producer'

    id = db.Column(db.Integer, primary_key=True)
    pivot_id = db.Column(db.Integer(), nullable=False)
    url_path = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)

    @property
    def url(self):
        return 'apipivots.io/pi/{}'.format(self.url_path)

class Hook(db.Model):

    __tablename__ = 'hook'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    repo_id = db.Column(db.Integer())
    repo_name = db.Column(db.String())
    repo_owner = db.Column(db.String())
    subscribe_uuid = db.Column(db.String())
    github_hook_secret = db.Column(db.String())
    github_hook_id = db.Column(db.Integer())

    def __init__(self, user_id, repo_id, repo_name, repo_owner, subscribe_uuid, github_hook_secret, github_hook_id):        
        self.user_id = user_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_owner = repo_owner
        self.subscribe_uuid = subscribe_uuid
        self.github_hook_secret = github_hook_secret
        self.github_hook_id = github_hook_id    


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    name = db.Column(db.String())
    email = db.Column(db.String())
    avatar_url = db.Column(db.String())
    company = db.Column(db.String())
    nb_followers = db.Column(db.Integer())
    nb_following = db.Column(db.Integer())
    github_access_token = db.Column(db.String(200))

    def __init__(self, github_access_token):
        self.github_access_token = github_access_token

    def pivots(self):
        """
        Return the pivots configured by the user
        """

        p1 = Pivot()
        p1.uuid = "helloworld"
        p1.user_id = self.id
        p1.name = "Sample pivot 1"
        p1.description = None
        p1.deleted = False
        p1.created_at = datetime.utcnow()
        p1.deleted_at = None

        p2 = Pivot()
        p2.uuid = "lkqsjdqdkj"
        p2.user_id = self.id
        p2.name = "Sample pivot 2"
        p2.description = None
        p2.deleted = False
        p2.created_at = datetime.utcnow()
        p2.deleted_at = None

        p3 = Pivot()
        p3.uuid = "qslkjhvbhj"
        p3.user_id = self.id
        p3.name = "Sample pivot 3"
        p3.description = None
        p3.deleted = False
        p3.created_at = datetime.utcnow()
        p3.deleted_at = None
        
        
        return [
            p1,
            p2,
            p3
        ]
        