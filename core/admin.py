# Importing necessary modules & libraries
from django.contrib import admin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SliderNumericFilter
from core.models import Tag, FundSource, Organization, Strategy, Initiative, SocialPost, Product, Consumer



# Changing some features of the admin site
admin.site.site_header = "Database administration"
admin.site.site_title = "Database administration"
admin.site.index_title = "TechShoi"



# Creating some admin classes for user-friendly Django model access
class TagAdmin(admin.ModelAdmin):
    list_display = ("value", )
    search_fields = ("value",)

class FundSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "email", "site", "funding_possibility")
    search_fields = ("name", "location", "email", "site")
    list_filter = ("funding_possibility", "related_tag")
    filter_horizontal = ("related_tag", )

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "category", "email", "site", "status")
    search_fields = ("name", "location", "email", "site")
    list_filter = ("category", "status", "funder", "related_tag")
    filter_horizontal = ("funder", "related_tag")

class StrategyAdmin(admin.ModelAdmin):
    list_display = ("name", "parent_org")
    search_fields = ("name", )
    list_filter = ("parent_org", "related_tag")
    filter_horizontal = ("related_tag",)

class InitiativeAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "link", "parent_org")
    search_fields = ("name", "link")
    list_filter = ("date", "parent_org", "followed_strategy", "related_tag")
    filter_horizontal = ("followed_strategy", "related_tag")

class SocialPostAdmin(admin.ModelAdmin):
    list_display = ("platform", "date", "link", "parent_org")
    search_fields = ("link", )
    list_filter = ("date", "platform", "parent_org", "followed_strategy", "related_tag")
    filter_horizontal = ("followed_strategy", "related_tag")

class ProductAdmin(NumericFilterModelAdmin, admin.ModelAdmin):
    list_display = ("name", "price", "date", "link", "parent_org")
    search_fields = ("name", "features")
    list_filter = (("price", SliderNumericFilter), "date", "parent_org", "related_tag")
    filter_horizontal = ("related_tag",)

class ConsumerAdmin(NumericFilterModelAdmin, admin.ModelAdmin):
    list_display = ("name", "email", "age", "location", "social_link")
    search_fields = ("name", "email", "location")
    list_filter = (("age", SliderNumericFilter), )



# Registering Django models.
admin.site.register(Tag, TagAdmin)
admin.site.register(FundSource, FundSourceAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(SocialPost, SocialPostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consumer, ConsumerAdmin)

