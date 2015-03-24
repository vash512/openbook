# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Deuda'
        db.create_table(u'libreta_deuda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['linku.Cliente'])),
            ('montoOriginal', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('deudaActual', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('individual', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
        ))
        db.send_create_signal(u'libreta', ['Deuda'])

        # Adding model 'Desglose'
        db.create_table(u'libreta_desglose', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deuda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['libreta.Deuda'])),
            ('producto', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal(u'libreta', ['Desglose'])

        # Adding model 'HistorialPago'
        db.create_table(u'libreta_historialpago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('deuda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['libreta.Deuda'])),
            ('pago', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('notas', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'libreta', ['HistorialPago'])


    def backwards(self, orm):
        # Deleting model 'Deuda'
        db.delete_table(u'libreta_deuda')

        # Deleting model 'Desglose'
        db.delete_table(u'libreta_desglose')

        # Deleting model 'HistorialPago'
        db.delete_table(u'libreta_historialpago')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'libreta.desglose': {
            'Meta': {'object_name': 'Desglose'},
            'deuda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['libreta.Deuda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'libreta.deuda': {
            'Meta': {'object_name': 'Deuda'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['linku.Cliente']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'deudaActual': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'individual': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'montoOriginal': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        u'libreta.historialpago': {
            'Meta': {'object_name': 'HistorialPago'},
            'deuda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['libreta.Deuda']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pago': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        u'linku.cliente': {
            'Meta': {'unique_together': "(('usuario', 'nombre'), ('correo', 'usuario'))", 'object_name': 'Cliente'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['libreta']