from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.
class Rank(models.Model):
    degree      = models.CharField(max_length = 20)
    color       = models.CharField(max_length = 20)
    position    = models.IntegerField()

    @property
    def slug(self):
        return slugify(self.color)

    @property
    def eligibility(self):
        return self.eligibility_set.all().order_by('position')

    @property
    def requirements(self):
        return self.requirement_set.all().order_by('category', 'position')

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('syllabi:rank_detail_view', args=[self.pk])

class Eligibility (models.Model):
    summary     = models.CharField(max_length = 20)
    position    = models.IntegerField()
    desc        = models.TextField(blank = True)
    rank        = models.ForeignKey(Rank, on_delete=models.CASCADE)

    def __str__(self):
        return self.summary

class Category (models.Model):
    name        = models.CharField(max_length = 20)
    position    = models.IntegerField()
    
    @property
    def requirements(self):
        return self.requirement_set.all().order_by('position')

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('syllabi:category_detail_view', args=[self.pk])

class Requirement (models.Model):
    slug        = models.SlugField(blank = True)
    name        = models.CharField(max_length = 100)
    position    = models.IntegerField(validators = [MinValueValidator(1)],)
    rank        = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    @property
    def media(self):
        return self.media_set.all().order_by('position')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('syllabi:requirement_detail_view', args=[self.rank.pk, self.category.pk, self.pk])

class Media (models.Model):
    file_name   = models.CharField(max_length = 20)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    desc        = models.TextField(blank = True)
    position    = models.IntegerField()
    
    def __str__(self):
        return self.file_name