from elasticsearch_dsl import Document, InnerDoc, Text, Integer, Long, Float, Nested, Date, Keyword
from elasticsearch_dsl.search import Q
from datetime import datetime


class IndexName:
    USER_INDEX = 'sample.user'


class UserSkillIndex(InnerDoc):
    skill_id = Integer()
    name = Text()
    name_keyword = Keyword()
    score = Float()


class UserIndex(Document):
    user_id = Long()
    name = Text()
    name_keyword = Keyword()
    skills = Nested(UserSkillIndex)
    created_at = Date()

    class Index:
        name = IndexName.USER_INDEX
        settings = {
            "number_of_shards": 2,
        }

    def save(self, **kwargs):
        self.created_at = datetime.now()
        self.name_keyword = self.name
        return super().save(**kwargs)

    def add_skill(self, skill_id, name, score):
        self.skills.append(UserSkillIndex(skill_id=skill_id, name=name, score=score,
                                          name_keyword=name))

    @staticmethod
    def search_by_skill_name(skill_name, using=None, index=None):
        skill_sort = {
            'skills.score': {
                'order': 'desc', 'mode': 'min', 'nested_path': 'skills',
                'nested_filter': {'match': {'skills.name': skill_name}}
            }
        }
        search_obj = UserIndex.search(using=using, index=index).query(
            "nested",
            path="skills",
            query=Q('match', **{'skills.name': skill_name})
        ).sort(skill_sort, '_score')
        return search_obj
