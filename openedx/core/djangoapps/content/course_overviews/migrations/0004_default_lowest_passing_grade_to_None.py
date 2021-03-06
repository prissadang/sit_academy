# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CourseOverview.lowest_passing_grade'
        db.alter_column('course_overviews_courseoverview', 'lowest_passing_grade', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'CourseOverview.lowest_passing_grade'
        db.alter_column('course_overviews_courseoverview', 'lowest_passing_grade', self.gf('django.db.models.fields.DecimalField')(default=0.5, max_digits=5, decimal_places=2))

    models = {
        'course_overviews.courseoverview': {
            'Meta': {'object_name': 'CourseOverview'},
            '_location': ('xmodule_django.models.UsageKeyField', [], {'max_length': '255'}),
            '_pre_requisite_courses_json': ('django.db.models.fields.TextField', [], {}),
            'advertised_start': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'cert_html_view_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cert_name_long': ('django.db.models.fields.TextField', [], {}),
            'cert_name_short': ('django.db.models.fields.TextField', [], {}),
            'certificates_display_behavior': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'certificates_show_before_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'course_image_url': ('django.db.models.fields.TextField', [], {}),
            'days_early_for_beta': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'display_name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'display_number_with_default': ('django.db.models.fields.TextField', [], {}),
            'display_org_with_default': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'end_of_course_survey_url': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'facebook_url': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'has_any_active_web_certificate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'primary_key': 'True', 'db_index': 'True'}),
            'lowest_passing_grade': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'mobile_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_sharing_url': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'visible_to_staff_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['course_overviews']