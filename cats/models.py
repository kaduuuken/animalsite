# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class CatProfile(models.Model):
	name = models.CharField(max_length=255)
	gender = models.SmallIntegerField(choices=((1, 'männlich'), (2, 'weiblich'), (3, 'unbekannt')))
	picture = models.ImageField(upload_to='cats')  #@todo upload to field
	race = models.CharField(max_length=255)
	birth_date = models.DateField()
	origin = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'cats'


class UserProfile(models.Model):
	user = models.ForeignKey(User)
	birth_date = models.DateField()
	picture = models.ImageField(upload_to='users')  #@todo upload to field
	address = models.ForeignKey('Address')

	def __unicode__(self):
		return str(self.user)

	class Meta:
		app_label = 'cats'


class Address(models.Model):
	## Street
	street = models.CharField(max_length=200, verbose_name=str("Straße"))

	## ZIP Code
	zip_code = models.CharField(max_length=200, verbose_name="Postleitzahl")

	## City
	city = models.CharField(max_length=200, verbose_name="Stadt")

	## Country
	country = models.CharField(max_length=200, verbose_name="Land")

	## returns street and city
	def __unicode__(self):
		return "%s, %s" % (self.street, self.city)

	class Meta:
		app_label = "cats"


class Doctor(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	address = models.ForeignKey('Address')
	website = models.URLField()

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'cats'


class OpeningHours(models.Model):
	from_hour = models.TimeField()
	to_hour = models.TimeField()
	day = models.SmallIntegerField(choices=((1, 'Montag'), (2, 'Dienstag'), (3, 'Mittwoch'), (4, 'Donnerstag'), (5, 'Freitag'), (6, 'Samstag'), (7, 'Sonntag')))
	doctor = models.ForeignKey('Doctor')

	def __unicode__(self):
		return "%s - %s" % (self.from_hour, self.to_hour)

	class Meta:
		app_label = 'cats'
