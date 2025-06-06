from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import registration
from PIL import Image
img = Image.new('RGB', (100, 100), color='white')
img.save(r"C:\\Users\\nisan\\OneDrive\\Desktop\\YONO\\media\\default.jpeg")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)