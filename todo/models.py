from django.db import models


# Create your models here.
class Item(models.Model):
    # null=false prevents items from being created without a name programatically
    # blank=false makes the field 'Required' on forms
    name = models.CharField(max_length=50, null=False, blank=False)
    complete = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
