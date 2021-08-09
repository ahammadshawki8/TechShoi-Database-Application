# Importing necessary modules & libraries
import uuid
from django.db import models



# Creating Django Models. Each represent a table.
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    value = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.value}"
    
    def save(self, *args, **kwargs):
        self.value = self.value.lower()
        return super(Tag, self).save(*args, **kwargs)


class FundSource(models.Model):
    FUND_POSSIBLE = [
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    site = models.URLField(unique=True, null=False, blank=False)
    funding_possibility = models.CharField(max_length=6, choices=FUND_POSSIBLE, default='Medium', null=False, blank=False)
    related_tag = models.ManyToManyField(Tag, related_name="funder_tag", blank=True)

    def __str__(self):
        return f"{self.name} • {self.funding_possibility}"
    
    def save(self, *args, **kwargs):
        self.location = self.location.title()
        return super(FundSource, self).save(*args, **kwargs)


class Organization(models.Model):
    ORGANIZATION_CATEGORY = [
        ('Competitor','Competitor'),
        ('Neutral','Neutral'),
        ('Market','Market'),
        ('Vendor','Vendor')
    ]

    ORGANIZATION_STATUS = [
       ('Active','Active'),
       ('Inactive','Inactive') 
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=10, choices=ORGANIZATION_CATEGORY, default='Neutral', null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    site = models.URLField(unique=True, null=True, blank=True)
    status = models.CharField(max_length=8, choices=ORGANIZATION_STATUS, default='Active', null=False, blank=False)
    funder = models.ManyToManyField(FundSource, related_name="funder", blank=True)
    related_tag = models.ManyToManyField(Tag, related_name="org_tag", blank=True)

    def __str__(self):
        return f"{self.name} • {self.category}"

    def save(self, *args, **kwargs):
        self.location = self.location.title()
        return super(Organization, self).save(*args, **kwargs)


class Strategy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.TextField(null=False, blank=False, unique=True)
    parent_org = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="strategy_org", null=True, blank=True)
    related_tag = models.ManyToManyField(Tag, related_name="strategy_tag", blank=True)

    def __str__(self):
        return f"{self.name}"


class Initiative(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.TextField(null=False, blank=False, unique=True)
    date = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    parent_org = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="initiative_org", null=True, blank=True)
    followed_strategy = models.ManyToManyField(Strategy, related_name="initiative_strategy", blank=True)
    related_tag = models.ManyToManyField(Tag, related_name="initiative_tag", blank=True)

    def __str__(self):
        return f"{self.name}"


class SocialPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    platform = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    link = models.URLField(null=False, blank=False)
    parent_org = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name="post_org", null=False, blank=False)
    followed_strategy = models.ManyToManyField(Strategy, related_name="post_strategy", blank=True)
    related_tag = models.ManyToManyField(Tag, related_name="post_tag", blank=True)

    def __str__(self):
        return f"{self.platform} • {self.parent_org.name}"
    
    def save(self, *args, **kwargs):
        self.platform = self.platform.lower()
        return super(SocialPost, self).save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    features = models.TextField(null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    parent_org = models.CharField(max_length=100, null=False, blank=False)
    related_tag = models.ManyToManyField(Tag, related_name="product_tag", blank=False)

    def __str__(self):
        return f"{self.name} • {self.price}"


class Consumer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=True, blank=True)
    age = models.IntegerField(null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    social_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.location = self.location.title()
        return super(Consumer, self).save(*args, **kwargs)
