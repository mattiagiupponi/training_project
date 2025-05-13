from django.db import models
from geonode.layers.models import Dataset
# Create your models here.

class CustomDataset(Dataset):

    long_descritption = models.TextField(verbose_name="Long Description")

    def is_a_dataset(self):
        return self.resource_type == 'dataset'
