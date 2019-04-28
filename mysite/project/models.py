from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to= "profile_pics")
    teacher_id = models.CharField(max_length=40, default=" ")
    student_id = models.CharField(max_length=40, default=" ")
    department = models.CharField(max_length=200, default=" ")
    hometown = models.CharField(max_length=200, default=" ")
    address = models.CharField(max_length=200, default=" ")
    dob = models.CharField(max_length=200, default=" ")
    blood_group = models.CharField(max_length=200, default=" ")
    institute = models.CharField(max_length=400, default=" ")

    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Personal_data(models.Model):
    student_id = models.CharField(max_length=40)
    department = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=200)
    institute = models.CharField(max_length=400)

class CT_Marks(models.Model):
    student_id = models.IntegerField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    course_name = models.CharField(max_length=40)
    CT_1 = models.IntegerField(max_length=40, default=" ")
    CT_2 = models.IntegerField(max_length=40, default=" ")
    CT_3 = models.IntegerField(max_length=40, default=" ")
    CT_4 = models.IntegerField(max_length=40, default=" ")




