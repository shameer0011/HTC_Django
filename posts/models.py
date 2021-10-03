from django.db import models
from blog.models import Post

# Create your models here.
class Posts(models.Model):
 
    image = models.ImageField(default='default.jpg', upload_to='post_pics')
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    
    def _str_(self):
        return f'{self.user.username} Posts'