from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import pymysql
from config import Config
from hashids import Hashids

app = Flask(__name__)
app.config.from_object(Config)

client = app.test_client()

# engine = create_engine('mysql+pymysql://user:123456@localhost/orm_test')
engine = create_engine('mysql+pymysql://root@localhost/orm_test')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


jwt = JWTManager(app)

salt = "это типа соль, бла бла бла"
hashids = Hashids(min_length=12, salt=salt)
user_id_hash = Hashids(min_length=8, salt=salt)


from models import *

# Создаем таблицы в БД
# Base.metadata.create_all(bind=engine)

@app.route('/register', methods=['POST'])
def register():
    params = request.json
    user = User(**params)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    user_id = user_id_hash.encode(user.id)
    return {'access_token': token, 'user_id': user_id}



@app.route('/<user_id>/links', methods=['GET'])
@jwt_required()
def get_list(user_id):
    user_id = user_id_hash.decode(user_id)
    links = Link.query.filter(Link.user_id == user_id[0])
    serialized = []
    for link in links:
        serialized.append({
            'id': link.id,
            'original': link.original,
            'short': f"{api_url}/{hashids.encode(link.id)}"
        })
    return jsonify(serialized)


@app.route('/<user_id>/links', methods=['POST'])
@jwt_required()
def update_list(user_id):
    user_id = user_id_hash.decode(user_id)
    print("ID Пользователя при добавлении ссылки", user_id[0])
    new_one = Link(**request.json)
    new_one.user_id = user_id
    session.add(new_one)
    session.commit()
    serialized = {
        'original': new_one.original,
        'user_id': user_id[0],
        'type_id': new_one.type_id,
        'counter': 0

    }
    return jsonify(serialized)


# @app.route('/<int:user_id>/links', methods=['PUT'])
# @jwt_required
# def update_tutorial(link_id):
#     user_id = get_jwt_identity()
#     item = Link.query.filter(Link.id == link_id).first()
#     params = request.json
#     if not item:
#         return {'message': 'Нет ссылок с таким id'}, 400
#     for key, value in params.items():
#         setattr(item, key, value)
#     session.commit()
#     serialized = {
#         'type_id': item.type_id
#     }
#     return serialized
#
#
# @app.route('/links/<int:link_id>', methods=['DELETE'])
# @jwt_required
# def delete_tutorial(link_id):
#     item = Link.query.filter(Link.id == link_id).first()
#     if not item:
#         return {'message': 'Нет ссылок с таким id'}, 400
#     session.delete(item)
#     session.commit()
#     return '', 204
#
#
@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


host = '10.170.1.120'
port = 8080
api_url = f"http://{host}:{port}"
if __name__ == '__main__':
    app.run(host=host, port=port)
