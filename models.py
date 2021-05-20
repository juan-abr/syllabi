from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.
class Rank(models.Model):
    degree      = models.CharField(max_length = 20)
    color       = models.CharField(max_length = 20, unique = True, verbose_name="color")
    position    = models.IntegerField(
        help_text="Position relative to other ranks."
    )
    slug        = models.SlugField(
        help_text= "This field should not be changed unless you KNOW what you are doing. I'm NOT kidding.",
        unique = True
    )

    @property
    def desc(self):
        return 'The requirements for the rank of %s %s at Central Maryland Martial Arts. Students must be eligible before they can test for %s' % (self.degree, self.color, self.color)

    @property
    def eligibility(self):
        return self.eligibility_set.all().order_by('position')

    @property
    def requirements(self):
        return self.requirement_set.all().order_by('category', 'position')

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        # return reverse('syllabi:rank_detail_view', args=[self.pk])
        return reverse('syllabi:rank_detail_view', kwargs={'slug': self.slug})

class Eligibility (models.Model):
    summary     = models.CharField(max_length = 20)
    position    = models.IntegerField()
    desc        = models.TextField(blank = True)
    rank        = models.ForeignKey(Rank, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Eligibilities"

    def __str__(self):
        return self.summary

class Category (models.Model):
    name        = models.CharField(max_length = 20, unique=True)
    position    = models.IntegerField()
    desc        = models.TextField(
        help_text="IMPORTANT: Google will use this as a preview snippet in the results of search. A description should be 1-2 sentences long preferably.",
        blank = True
    )
    slug        = models.SlugField(
        help_text= "This field should not be changed unless you KNOW what you are doing. I'm NOT kidding.",
        unique = True
    )

    class Meta:
        verbose_name_plural = "Categories"
    
    @property
    def requirements(self):
        return self.requirement_set.all().order_by('position')

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        # return reverse('syllabi:category_detail_view', args=[self.pk])
        return reverse('syllabi:category_detail_view', kwargs={'slug': self.slug})


class Requirement (models.Model):
    name        = models.CharField(max_length = 100, unique=True)
    position    = models.IntegerField(validators = [MinValueValidator(1)],)
    rank        = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    desc        = models.TextField(blank=True)
    slug        = models.SlugField(
        help_text="This field should not be changed unless you KNOW what you are doing. I'm NOT kidding.",
        unique = True
    )

    @property
    def media(self):
        return self.media_set.all().order_by('position')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('syllabi:requirement_detail_view', args=[self.rank.pk, self.category.pk, self.pk])
        return reverse('syllabi:requirement_detail_view',
            kwargs={
                'rank_slug': self.rank.slug,
                'category_slug': self.category.slug,
                'requirement_slug': self.slug
            })

class Media (models.Model):
    file_name   = models.CharField(max_length = 20)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    desc        = models.TextField(blank = True)
    position    = models.IntegerField()

    class Meta:
        verbose_name_plural = "Media"
    
    def __str__(self):
        return self.file_name