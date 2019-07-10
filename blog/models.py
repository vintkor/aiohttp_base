from tortoise import fields, Model


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)

    def __str__(self):
        return self.title[:150]
