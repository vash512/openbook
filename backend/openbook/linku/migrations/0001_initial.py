# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'linku_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('direccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'linku', ['Cliente'])

        # Adding unique constraint on 'Cliente', fields ['usuario', 'nombre']
        db.create_unique(u'linku_cliente', ['usuario_id', 'nombre'])

        # Adding unique constraint on 'Cliente', fields ['correo', 'usuario']
        db.create_unique(u'linku_cliente', ['correo', 'usuario_id'])

        # Adding model 'Telefono'
        db.create_table(u'linku_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['linku.Cliente'])),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'linku', ['Telefono'])

        # Adding unique constraint on 'Telefono', fields ['cliente', 'telefono']
        db.create_unique(u'linku_telefono', ['cliente_id', 'telefono'])

        # Adding model 'GrupoCliente'
        db.create_table(u'linku_grupocliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'linku', ['GrupoCliente'])

        # Adding M2M table for field cliente on 'GrupoCliente'
        m2m_table_name = db.shorten_name(u'linku_grupocliente_cliente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('grupocliente', models.ForeignKey(orm[u'linku.grupocliente'], null=False)),
            ('cliente', models.ForeignKey(orm[u'linku.cliente'], null=False))
        ))
        db.create_unique(m2m_table_name, ['grupocliente_id', 'cliente_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Telefono', fields ['cliente', 'telefono']
        db.delete_unique(u'linku_telefono', ['cliente_id', 'telefono'])

        # Removing unique constraint on 'Cliente', fields ['correo', 'usuario']
        db.delete_unique(u'linku_cliente', ['correo', 'usuario_id'])

        # Removing unique constraint on 'Cliente', fields ['usuario', 'nombre']
        db.delete_unique(u'linku_cliente', ['usuario_id', 'nombre'])

        # Deleting model 'Cliente'
        db.delete_table(u'linku_cliente')

        # Deleting model 'Telefono'
        db.delete_table(u'linku_telefono')

        # Deleting model 'GrupoCliente'
        db.delete_table(u'linku_grupocliente')

        # Removing M2M table for field cliente on 'GrupoCliente'
        db.delete_table(db.shorten_name(u'linku_grupocliente_cliente'))


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
        u'linku.cliente': {
            'Meta': {'unique_together': "(('usuario', 'nombre'), ('correo', 'usuario'))", 'object_name': 'Cliente'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'linku.grupocliente': {
            'Meta': {'object_name': 'GrupoCliente'},
            'cliente': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['linku.Cliente']", 'symmetrical': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'linku.telefono': {
            'Meta': {'unique_together': "(('cliente', 'telefono'),)", 'object_name': 'Telefono'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['linku.Cliente']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['linku']