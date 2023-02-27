from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def __str__(self) -> str:
        return self.name
        
    def children(self):
        return self.menu_set.all()

    def get_parent_id(self):
        if self.parent:
            return self.parent.get_parent_id() + [self.parent.id]
        else:
            return []