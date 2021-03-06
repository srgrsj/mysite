from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)
