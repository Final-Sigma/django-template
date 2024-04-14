from django.urls import path
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from example_blog.models import BlogPost

class BlogPostsSitemap(Sitemap):
    def items(self):
        return BlogPost.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
    
def SitemapURL():
    return path(
        'sitemap.xml',
        sitemap,
        {
            'sitemaps': {
                'posts': BlogPostsSitemap
            },
        },
        name="django.contrib.sitemaps.views.sitemap",
    )