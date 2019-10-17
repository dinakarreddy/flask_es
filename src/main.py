from flask import Flask, request, abort
from config.settings import *
from es_models import UserIndex

if INIT_ES_INDEX:
    from scripts.init_es.main import main as init_es

    init_es()

app = Flask(__name__)


@app.route("/get-users")
def get_users():
    skill_name = request.args.get('skill_name')
    if not skill_name:
        abort(400)
    data = UserIndex.search_by_skill_name(skill_name).execute()
    return data.to_dict()
