from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    photo = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.username

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '%s to %s' % (self.from_user.username, self.to_user.username)
