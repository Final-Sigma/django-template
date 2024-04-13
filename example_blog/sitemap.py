# reference: https://docs.djangoproject.com/en/5.0/ref/contrib/sitemaps/

from django.contrib.sitemaps import Sitemap
from .models import BlogPost

# TODO: Add 'last modified' datetime to BlogPost to allow sitemap
#       to stay up to date with latest changes.

# TODO: Add BlogPost.get_absolute_url() to model and follow
#       this tutorial to build it correctly:
#       https://learndjango.com/tutorials/django-sitemap-tutorial

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return BlogPost.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date