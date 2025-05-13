import uuid
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404
from geonode.base.models import ResourceBase
from geonode.layers.models import Dataset
from training.example.models import CustomDataset
from geonode.resource.manager import resource_manager
# Create your views here.


def serve_training(request):
    # python code
    dataset_list = Dataset.objects.all()
    output = [
        {
            "title": dataset.title,
            "pk": dataset.pk,
        }
        for dataset in dataset_list
    ]
    return JsonResponse(output, safe=False)


def insert_custom(request):
    # python code
    dataset_pk = request.GET.get("pk")
    description = request.GET.get("description")

    resource = resource_manager.create(
        str(uuid.uuid4()),
        resource_type=Dataset,
        defaults={
            "title": "my_title",
            "owner": request.user
        }
    )
    
    return JsonResponse({"created": True, "pk": resource.pk}, safe=False)
