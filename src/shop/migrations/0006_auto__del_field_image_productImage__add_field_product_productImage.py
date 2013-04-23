# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
  def forwards(self, orm):
    # Deleting field 'Image.productImage'
    db.delete_column('shop_image', 'productImage_id')

    # Adding field 'Product.productImage'
    db.add_column('shop_product', 'productImage',
      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Image'], null=True),
      keep_default=False)


  def backwards(self, orm):
    # Adding field 'Image.productImage'
    db.add_column('shop_image', 'productImage',
      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shop.Product'], null=True),
      keep_default=False)

    # Deleting field 'Product.productImage'
    db.delete_column('shop_product', 'productImage_id')


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
    'shop.division': {
      'Meta': {'object_name': 'Division'},
      'divisionName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
    },
    'shop.image': {
      'Meta': {'object_name': 'Image'},
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'imageFile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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
      'division': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Division']", 'null': 'True'}),
      'endurance': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
      'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
      'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
      'label': ('django.db.models.fields.related.ManyToManyField', [],
                {'symmetrical': 'False', 'to': "orm['shop.Label']", 'null': 'True', 'blank': 'True'}),
      'pricePerUnit': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
      'producer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Producer']"}),
      'productImage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Image']", 'null': 'True'}),
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