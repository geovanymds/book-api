from tortoise.models import Model
from tortoise import fields


class Books(Model):
    book_id: int = fields.IntField(pk=True)
    magic_code: str = fields.CharField(max_length=45, null=False, unique=True)
    title: str = fields.CharField(max_length=256, null=False)
    author: str = fields.CharField(max_length=256, null=False)
    total_pages: int = fields.IntField(default=0)
    total_images: int = fields.IntField(default=0)

    def __str__(self):
        return self.title
