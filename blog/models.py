from django.db import models

# Create your models here.
class Blogs(models.Model):
    title =models.CharField(max_length=150)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
     
    def __str__(self):
        return self.title
    def summary(self):
        return self.content[:100] + "...."
    
class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    email = models.EmailField(blank=False)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Contact_me(models.Model):
    email = models.EmailField(blank=False)
    subject = models.TextField()
    message = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    
