from django.contrib import admin

from .models import Manufacturer, SinglePod, SinglePodStock, SinglePodImages, Taste

admin.site.register(Manufacturer)
admin.site.register(SinglePod)
admin.site.register(SinglePodImages)
admin.site.register(SinglePodStock)
admin.site.register(Taste)

