from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tags(models.Model):
    id_tag = models.AutoField(primary_key=True)
    name=models.CharField( max_length=100)
    def __str__(self):
        return f'{self.name} '

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    tag=models.ForeignKey(tags , on_delete=models.CASCADE)
    description=models.TextField()
    link=models.URLField(blank=True,default="")
    create_at = models.DateField (auto_now_add=True)
    image=models.ImageField(upload_to='post',null=True,blank= True)
    
    def __str__(self):
        return f'Author {self.author.username} - Tittle {self.title}'

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=150, default='Sin Nombre')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    Date_coment=models.DateField (auto_now_add=True)

    def __str__(self):
        return '%s - %s ' % (self.post.title , self.name)