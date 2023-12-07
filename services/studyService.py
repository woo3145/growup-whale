import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from services import loginService, registerService, dataService, studyService
from app import User, Studytypelevel, Whale, db

app = Flask(__name__)


# # 레벨 구하기
def get_level(required_exp, total_exp) :
    level = 0
    if total_exp < required_exp["2"] : level = 1
    elif total_exp < required_exp["3"] : level = 2
    elif total_exp < required_exp["4"] : level = 3
    elif total_exp < 99 : level = 4
    elif total_exp >= 99 : level = 5
    return level


# 버튼 클릭 시 진행
def studyCheck(db, required_exp) :
    print("studyEnd", required_exp)

    # 유저 아이디 받아오기
    # id = 

    # 클릭한 버튼 찾아내기
    # study_type =   

    # 해당 study_type에 경험치 추가해주기 (일단 blog_lv에 추가로 작성)
    studytype_list = db.Studytypelevel.filter_by(id=1).first()
    studytype_list.blog_lv = studytype_list[0].blog_lv + 1
    db.sesseion.add(studytype_list)
    db.session.commit()

    # study_type 중에 제일 높은 숫자를 가진걸로 job 설정
    studytype_list = db.studytypelevel.filter_by(id=1).first()
    data = {
        'blog_lv' : studytype_list[0].blog_lv,
        'algorithm_lv' : studytype_list[0].algorithm_lv,
        'main_lv' : studytype_list[0].main_lv,
        'cs' : studytype_list[0].cs_lv
    }
    job = max(data, key=data.get)
    max_exp = max(data.values())

    # 총 경험치와 레벨을 계산하여 DB에 기록 (whale -> level, exp)
    total_exp = sum(data.values())
    print(total_exp)

    whale_list = db.whale.filter_by(id=1).first()
    whale_list[0].level = get_level(required_exp, total_exp)
    whale_list[0].job = job
    whale_list[0].exp = max_exp
    db.session.add(whale_list)
    db.session.commit()



    # return {
    #     success : 
    # }

    # try :
    # except :