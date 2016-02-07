# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # loading fixture
        from django.core.management import call_command
        call_command("loaddata", "apps/hello/fixtures/initial_data.json")
        

    def backwards(self, orm):
        pass


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['hello']