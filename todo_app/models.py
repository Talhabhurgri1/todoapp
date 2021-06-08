from django.db import models

# Create your models here.
class TodoApp(models.Model):

    items_added = models.CharField(max_length=200,null="True")
    def __str__(self):
        return 'ITEM:{0}'.format(self.items_added)
