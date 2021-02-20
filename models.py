from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Rank(models.Model):
    slug        = models.SlugField(blank = True)
    degree      = models.CharField(max_length = 20)
    color       = models.CharField(max_length = 20)
    position    = models.IntegerField()

    def __str__(self):
        return self.color

    @property
    def eligibility(self):
        return self.eligibility_set.all().order_by('position')

    @property
    def requirements(self):
        return self.requirement_set.all().order_by('category', 'position')

class Eligibility (models.Model):
    summary     = models.CharField(max_length = 20)
    position    = models.IntegerField()
    desc        = models.TextField(blank = True)
    rank        = models.ForeignKey(Rank, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary

class Category (models.Model):
    slug        = models.SlugField(blank = True)
    name        = models.CharField(max_length = 20)
    position    = models.IntegerField()

    def __str__ (self):
        return self.name
    
    @property
    def requirements(self):
        return self.requirement_set.all().order_by('position')

class Requirement (models.Model):
    slug        = models.SlugField(blank = True)
    name        = models.CharField(max_length = 100)
    position    = models.IntegerField(
                    # unique = True,
                    validators = [MinValueValidator(1)],
                )
    rank        = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    @property
    def media(self):
        return self.media_set.all().order_by('position')

    # @property
    # def categories(self):
    #     return self.category_set.all().order_by('position')

class Media (models.Model):
    file_name   = models.CharField(max_length = 20)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    desc        = models.TextField(blank = True)
    position    = models.IntegerField()