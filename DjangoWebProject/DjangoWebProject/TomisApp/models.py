from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
# Create your models here.


class Tomis(models.Model):
	AccountDescriptiveName = models.CharField(max_length=200)
	CampaignId = models.CharField(max_length=200) 
	CampaignName = models.CharField(max_length=200)
	CampaignStatus = models.CharField(max_length=200)
	CityCriteriaId = models.CharField(max_length=200)
	CountryCriteriaId = models.CharField(max_length=200)
	CustomerDescriptiveName = models.CharField(max_length=200)
	ExternalCustomerId = models.CharField(max_length=200)
	IsTargetingLocation = models.CharField(max_length=200)
	MetroCriteriaId = models.CharField(max_length=200)
	MostSpecificCriteriaId = models.CharField(max_length=200)
	RegionCriteriaId = models.CharField(max_length=200)
	Date = models.CharField(max_length=200)
	Device = models.CharField(max_length=200)
	LocationType = models.CharField(max_length=200)
	AveragePosition = models.CharField(max_length=200)
	Clicks = models.IntegerField(default=0)
	Conversions = models.CharField(max_length=200)
	ConversionValue = models.CharField(max_length=200)
	Cost = models.CharField(max_length=200)
	Impressions = models.CharField(max_length=200)
	Interactions = models.CharField(max_length=200)
	InteractionTypes = models.CharField(max_length=200)
	VideoViews = models.CharField(max_length=200)

def __unicode__(self):
        return u"%s" % self.name