# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
  def forwards(self, orm):
    # Adding model 'Address'
    db.create_table('shop_address', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('surName', self.gf('django.db.models.fields.CharField')(max_length=150)),
      ('firstName', self.gf('django.db.models.fields.CharField')(max_length=50)),
      ('streetName', self.gf('django.db.models.fields.CharField')(max_length=100)),
      ('zipCode', self.gf('django.db.models.fields.IntegerField')()),
      ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
      ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
      ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
      ))
    db.send_create_signal('shop', ['Address'])

    # Adding model 'Label'
    db.create_table('shop_label', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('labelName', self.gf('django.db.models.fields.CharField')(max_length=25)),
      ))
    db.send_create_signal('shop', ['Label'])

    # Adding model 'Category'
    db.create_table('shop_category', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('categoryName', self.gf('django.db.models.fields.CharField')(max_length=50)),
      ))
    db.send_create_signal('shop', ['Category'])

    # Adding model 'Producer'
    db.create_table('shop_producer', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Address'])),
      ('shortName', self.gf('django.db.models.fields.CharField')(max_length=70)),
      ))
    db.send_create_signal('shop', ['Producer'])

    # Adding model 'Product'
    db.create_table('shop_product', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('producer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Producer'])),
      ('headline', self.gf('django.db.models.fields.CharField')(max_length=200)),
      ('description', self.gf('django.db.models.fields.TextField')()),
      ('publishDate', self.gf('django.db.models.fields.DateTimeField')()),
      ('quantityUnit', self.gf('django.db.models.fields.CharField')(max_length=20)),
      ('endurance', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
      ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
      ('pricePerUnit', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
      ))
    db.send_create_signal('shop', ['Product'])

    # Adding M2M table for field label on 'Product'
    db.create_table('shop_product_label', (
      ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
      ('product', models.ForeignKey(orm['shop.product'], null=False)),
      ('label', models.ForeignKey(orm['shop.label'], null=False))
      ))
    db.create_unique('shop_product_label', ['product_id', 'label_id'])

    # Adding M2M table for field category on 'Product'
    db.create_table('shop_product_category', (
      ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
      ('product', models.ForeignKey(orm['shop.product'], null=False)),
      ('category', models.ForeignKey(orm['shop.category'], null=False))
      ))
    db.create_unique('shop_product_category', ['product_id', 'category_id'])

    # Adding model 'Image'
    db.create_table('shop_image', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('path', self.gf('django.db.models.fields.CharField')(max_length=200)),
      ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'])),
      ))
    db.send_create_signal('shop', ['Image'])

    # Adding model 'UserProfile'
    db.create_table('shop_userprofile', (
      ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
      ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
      ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Address'])),
      ))
    db.send_create_signal('shop', ['UserProfile'])


  def backwards(self, orm):
    # Deleting model 'Address'
    db.delete_table('shop_address')

    # Deleting model 'Label'
    db.delete_table('shop_label')

    # Deleting model 'Category'
    db.delete_table('shop_category')

    # Deleting model 'Producer'
    db.delete_table('shop_producer')

    # Deleting model 'Product'
    db.delete_table('shop_product')

    # Removing M2M table for field label on 'Product'
    db.delete_table('shop_product_label')

    # Removing M2M table for field category on 'Product'
    db.delete_table('shop_product_category')

    # Deleting model 'Image'
    db.delete_table('shop_image')

    # Deleting model 'UserProfile'
    db.delete_table('shop_userprofile')


  models = {
    'auth.group': {
      'Meta': {'object_name': 'Group'},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
      'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                      {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
    },
    'auth.permission': {
      'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')",
               'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
      'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
    },
    'auth.user': {
      'Meta': {'object_name': 'User'},
      'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
      'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
      'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
      'groups': ('django.db.models.fields.related.ManyToManyField', [],
                 {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
      'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
      'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
      'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
      'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                           {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
      'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
    },
    'contenttypes.contenttype': {
      'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType',
               'db_table': "'django_content_type'"},
      'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
    },
    'shop.address': {
      'Meta': {'object_name': 'Address'},
      'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
      'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'streetName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
      'surName': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
      'zipCode': ('django.db.models.fields.IntegerField', [], {})
    },
    'shop.category': {
      'Meta': {'object_name': 'Category'},
      'categoryName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
    },
    'shop.image': {
      'Meta': {'object_name': 'Image'},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"})
    },
    'shop.label': {
      'Meta': {'object_name': 'Label'},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'labelName': ('django.db.models.fields.CharField', [], {'max_length': '25'})
    },
    'shop.producer': {
      'Meta': {'object_name': 'Producer'},
      'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Address']"}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'shortName': ('django.db.models.fields.CharField', [], {'max_length': '70'})
    },
    'shop.product': {
      'Meta': {'object_name': 'Product'},
      'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
      'category': (
      'django.db.models.fields.related.ManyToManyField', [], {'to': "orm['shop.Category']", 'symmetrical': 'False'}),
      'description': ('django.db.models.fields.TextField', [], {}),
      'endurance': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
      'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'label': ('django.db.models.fields.related.ManyToManyField', [],
                {'symmetrical': 'False', 'to': "orm['shop.Label']", 'null': 'True', 'blank': 'True'}),
      'pricePerUnit': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
      'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Producer']"}),
      'publishDate': ('django.db.models.fields.DateTimeField', [], {}),
      'quantityUnit': ('django.db.models.fields.CharField', [], {'max_length': '20'})
    },
    'shop.userprofile': {
      'Meta': {'object_name': 'UserProfile'},
      'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Address']"}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
    }
  }

  complete_apps = ['shop']