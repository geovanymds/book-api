from tortoise.models import Model
from tortoise import fields

class Pages(Model):
  page_id: int = fields.IntField(pk=True)
  page_number: int = fields.IntField(default=0)
  page_text: str = fields.CharField(max_length=1500)
  book_id: int = fields.ForeignKeyField('models.Books', related_name='owned_page')
  def __str__(self):
    return self.page_id