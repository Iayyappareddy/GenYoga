from django.db import models
class YogaPose(models.Model):
    LEVEL_CHOICE=[
        ('beginner','Beginner'),
        ('intermediate','Intermediate'),
        ('advanced','Advanced'),
    ]
    BODY_PART=[
        ('neck','Neck'),
        ('knee','Knee'),
        ('back','Back'),
    ]
    name=models.CharField(max_length=50)
    body_part=models.CharField(max_length=10,choices=BODY_PART)
    pain_level=models.CharField(max_length=20,choices=LEVEL_CHOICE)
    instuctions=models.CharField(max_length=500)
    benifits=models.CharField(max_length=500)
    image = models.ImageField(upload_to='yoga_images/',null=True,blank=True)
    def __str__(self):
        return self.name
