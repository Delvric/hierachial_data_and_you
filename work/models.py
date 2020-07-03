from django.db import models
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class File_System(MPTTModel):
    name = models.CharField(max_length=40, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
# Create your models here.
