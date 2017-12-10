# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import *

def program_release_count(program):
	return program.releases.count()
program_release_count.short_description = 'number of releases'

def program_last_release(program):
	return program.releases.last().number if program.releases.count() > 0 else None
program_last_release.short_description = 'latest release'

class ProgramAdmin(admin.ModelAdmin):
	list_display = ('name', program_release_count, program_last_release)

admin.site.register(Program, ProgramAdmin)

class TrackInline(admin.TabularInline):
	model = Track
	extra = 0

def release_program_name(release):
	return release.program.name
release_program_name.short_description = 'program'

def release_track_count(release):
	return release.tracks.count()
release_track_count.short_description = 'number of tracks'

class ReleaseAdmin(admin.ModelAdmin):
	list_display = ('program', 'number', release_track_count)
	list_display_links = ('number',)
	inlines = [TrackInline]

admin.site.register(Release, ReleaseAdmin)

