from tortoise.models import Model
from tortoise import fields


class Images(Model):
    image_id: int = fields.IntField(pk=True)
    url: str = fields.CharField(max_length=256, null=False, unique=True)
    name: str = fields.CharField(max_length=256, null=False)
    path: str = fields.CharField(max_length=256, null=False)
    book: int = fields.ForeignKeyField(
        'models.Books', related_name='owned_image')

    def __str__(self):
        return self.original_name
