from django.contrib import admin
from core.models import Tag, FundSource, Organization, Strategy, Initiative, SocialPost, Product, Consumer


# Register your models here.
admin.site.site_header = "Database administration"
admin.site.site_title = "Database administration"
admin.site.index_title = "TechShoi"

admin.site.register(Tag)
admin.site.register(FundSource)
admin.site.register(Organization)
admin.site.register(Strategy)
admin.site.register(Initiative)
admin.site.register(SocialPost)
admin.site.register(Product)
admin.site.register(Consumer)
