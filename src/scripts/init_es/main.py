from scripts.init_es.data import SAMPLE_DATA
from es_models import UserIndex, IndexName
from elasticsearch_dsl import Index
from elasticsearch.helpers import bulk
from config.settings import ES_CLIENT

from elasticsearch.exceptions import NotFoundError


def insert_batch(actions):
    bulk(client=ES_CLIENT, actions=actions)


def init_user_index_data():
    batch_size = 10
    for i in range(0, len(SAMPLE_DATA), batch_size):
        batch = SAMPLE_DATA[i:i + batch_size]
        actions = []
        for data in batch:
            user_obj = UserIndex(user_id=data['user_id'], name=data['name'],
                                 name_keyword=data['name'])
            for skill_data in data.get('skills', []):
                user_obj.add_skill(skill_data['skill_id'], skill_data['name'], skill_data['score'])
            user_obj.save()
            # Instead of saving individual obj, can insert in bulk by the below code
            # actions.append(user_obj.to_dict(include_meta=True))
            # insert_batch(actions)


def delete_and_recreate_index():
    index_names = [IndexName.USER_INDEX]
    for index in index_names:
        try:
            Index(index).delete()
        except NotFoundError:
            pass
    UserIndex.init()


def main():
    delete_and_recreate_index()
    init_user_index_data()


if __name__ == '__main__':
    main()
