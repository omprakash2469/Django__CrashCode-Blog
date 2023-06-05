from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blogs.models import Blogs, Categories

class CategorieSitemap(Sitemap):
    def items(self):
        return Categories.objects.all()
    
class BlogsSitemap(Sitemap):
    def items(self):
        return Blogs.objects.filter(status=Blogs.ACTIVE)
    
    def last_mode(self, obj):
        return obj.created_at