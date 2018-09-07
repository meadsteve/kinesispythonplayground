import json

from mimesis import Person
from boto import kinesis
from json import JSONEncoder

class DictEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__


class User():

    def __init__(self):
        source = Person('en')
        self.first_name = source.name()
        self.last_name = source.last_name()

    def __str__(self):
        return f"PERSON: {self.first_name} {self.last_name}"


kinesis = kinesis.connect_to_region("eu-west-1")

for _ in range(10):
    user = User()
    print(user)
    kinesis.put_record("BotoDemo", json.dumps(user, cls=DictEncoder), "partitionkey")