from django.db import models
from thumbs import ImageWithThumbsField

class Picture(models.Model):
    image = ImageWithThumbsField(upload_to='images', sizes=((200,200),))

