from tortoise.models import Model
from tortoise import fields


class Pages(Model):
    page_id: int = fields.IntField(pk=True)
    number: int = fields.IntField(default=1)
    text: str = fields.CharField(max_length=1500)
    book: int = fields.ForeignKeyField(
        'models.Books', related_name='owned_page')

    def __str__(self):
        return self.page_id
