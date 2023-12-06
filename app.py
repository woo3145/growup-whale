# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from services import loginService, studyService

app = Flask(__name__)

# DB

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), nullable=False)
    starttime = db.Column(db.String(10000), nullable=False)

    whale_id = db.Column(db.Integer, db.ForeignKey("whale.id"))
    whale = relationship("whale", back_populates="user")
    study_type_level_id = db.Column(
        db.Integer, db.ForeignKey("studytypelevel.id"))
    study_type_level = relationship("studytypelevel", back_populates="user")


class Whale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(100), nullable=False)
    job = db.Column(db.String(100), nullable=False)
    exp = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Studytypelevel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_lv = db.Column(db.String(100), nullable=False)
    argorithm_lv = db.Column(db.String(100), nullable=False)
    main_lv = db.Column(db.String(100), nullable=False)
    cs_lv = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template('main.html')


@app.route("/login")
def login():
    loginService.userLogin()
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
