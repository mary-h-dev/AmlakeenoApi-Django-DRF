from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model
User=get_user_model()
import PIL
from django.core.files import File
from io import BytesIO


"""
compress images
"""
def compress(picture):
    if picture:
        pic= PIL.Image.open(picture)
        buf=BytesIO()
        pic.save(buf,'JPEG', quality=35)
        new_pic=File(buf, name=picture.name)
        return new_pic
    else:
        return None



"""
for post model
"""
class Post(models.Model):
    post_name = models.CharField(max_length=32, null=False, unique=False)
    description = models.TextField()
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(('Post Image'), upload_to='post/post_cover/', blank=True,)

    


    def __str__(self):
        return self.post_name
    
   

    def save(self,*args,**kwargs):
        new_picture=compress(self.image)
        self.image=new_picture
        super().save(*args,**kwargs)


"""
for comments
"""
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

def __str__(self):
    return self.user


"""
for like model
"""
class PostLikeDislike(models.Model):
    post = models.ForeignKey(Post, related_name='LikedislikedPost', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='LikedislikedUser',  on_delete=models.CASCADE)
    like = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user', 'post']

