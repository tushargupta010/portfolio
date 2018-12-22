from django.db import models

# Create your models here.
#title
#pub_date
#image
#body

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title



#add blog app to the settings

#create a migrations

#migrate

#add app to admin
