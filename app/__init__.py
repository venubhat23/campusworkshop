"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq3282qv2dcb92fo2g-a.oregon-postgres.render.com",
        database="todo_2yj5",
        user="root",
        password="dKjMXsJNsBeNjmupiXZO54bVPChYlseo")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
