from django.db import models

class Usern(models.Model):
    ID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50, default='00000000')

    def __str__(self):
        return f"{self.ID} {self.username}"

class Post(models.Model):
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date_published = models.DateField(null=True)

    def __str__(self):
        return f"{self.ID} {self.title}"

class Comment(models.Model):
    ID = models.IntegerField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Usern, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    date_posted = models.DateField(null=True)

    def __str__(self):
        return f"{self.ID}"

class Category(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ID}"