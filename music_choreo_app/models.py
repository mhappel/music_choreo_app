# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Program(models.Model):
	name = models.CharField(max_length=20, unique = True)

	class Meta: 
		ordering = ('name',)
	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name	


class Release(models.Model):
	number = models.PositiveSmallIntegerField('release number')
	program = models.ForeignKey(Program, models.CASCADE, related_name = 'releases')

	class Meta:
		ordering = ('number',)
		unique_together = ('number', 'program')
	def __str__(self):
		return '{:} {:}'.format(self.program, self.number)
	def __unicode__(self):
		return u'{:} {:}'.format(self.program, self.number)
		

class Track(models.Model):
	number = models.PositiveSmallIntegerField('track number')
	name = models.CharField(max_length=50)
	release = models.ForeignKey(Release, models.CASCADE, related_name = 'tracks')
	length = models.FloatField()

	class Meta:
		ordering = ('number',)
		unique_together = ('number', 'release')			
		