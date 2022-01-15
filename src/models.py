from tortoise.models import Model
from tortoise import fields

class Books(Model):
  book_id: int = fields.IntField(pk=True)
  magic_code: str = fields.CharField(max_length=45, null=False, unique=True)
  title: str = fields.CharField(max_length=256,null=False)
  author: str = fields.CharField(max_length=256,null=False)
  total_pages: int = fields.IntField(default=0)
  total_images: int = fields.IntField(default=0)
  def __str__(self):
    return self.name

class Pages(Model):
  page_id: int = fields.IntField(pk=True)
  page_number: int = fields.IntField(default=0)
  page_text: str = fields.CharField(max_length=1500)
  book_id: int = fields.ForeignKeyField('models.Books', related_name='owned_page')
  def __str__(self):
    return self.page_id

class Images(Model):
  image_id: int = fields.IntField(pk=True)
  url: str = fields.CharField(max_length=256, null=False, unique=True)
  image_format: str = fields.CharField(max_length=5,null=False)
  original_name: str = fields.CharField(max_length=256,null=False)
  path: str = fields.CharField(max_length=256,null=False)
  size: int = fields.IntField(default=0)
  book_id: int = fields.ForeignKeyField('models.Books', related_name='owned_image')
  def __str__(self):
    return self.name