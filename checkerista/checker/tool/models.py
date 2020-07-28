from django.db import models



class text(models.Model):
    Content = models.TextField()

    #text_id = models.ForeignKey(text, on_delete=models.CASCADE)
class compare(models.Model):
    comparison= models.TextField()

#class url(models.Model):
 #  Content= models.URLField()
  # pub_date = models.DateTimeField('entry date')