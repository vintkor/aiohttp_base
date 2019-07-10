from tortoise import fields, Model


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)

    def __str__(self):
        return self.title[:150]

    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def to_json(self, to_serialize: list) -> dict:
        d = {}
        for attr_name in to_serialize:
            d[attr_name] = getattr(self, attr_name)
        return d
