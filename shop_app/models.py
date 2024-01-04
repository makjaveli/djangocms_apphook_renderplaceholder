from django.db import models

from cms.models.fields import Placeholder, PlaceholderRelationField
from cms.utils.placeholder import get_placeholder_from_slot
from django.utils.functional import cached_property

class Product(models.Model):
    product_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=64)
    available = models.BooleanField(default = False)

    placeholders = PlaceholderRelationField()

    def _get_placeholder_from_slot(self, slotname):
        try:
            return self.placeholders.get(slot=slotname)
        except Placeholder.DoesNotExist:
            from cms.utils.placeholder import rescan_placeholders_for_obj
            rescan_placeholders_for_obj(self)
            return self.placeholders.get(slot=slotname)


    @cached_property
    def description(self):
#   	     return self._get_placeholder_from_slot("product_description")               
        return get_placeholder_from_slot(self.placeholders, "product_description")


    def __str__(self):
	    return self.product_title

