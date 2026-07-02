from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name


class Place(models.Model):
    external_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class ProjectPlace(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='place')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, default='')
    visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('project', 'place')