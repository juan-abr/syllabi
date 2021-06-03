from django.contrib.sitemaps import Sitemap

from .models import Rank, Category, Requirement

class RankSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Rank.objects.all()

    # def lastmod(self, obj):
    #     return obj.updated

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.all()

    # def lastmod(self, obj):
    #     return obj.updated

class RequirementSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Requirement.objects.all()
    
    # def lastmod(self, obj):
    #     return obj.updated