# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json

from django.db.models import TextField
from django.utils import six

from django_mysql.compat import field_class

__all__ = ('JSONField',)


class JSONField(field_class(TextField)):
    def __init__(self, *args, **kwargs):
        if 'default' not in kwargs:
            kwargs['default'] = dict
        super(JSONField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(JSONField, self).deconstruct()
        path = 'django_mysql.models.%s' % self.__class__.__name__
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'json'

    def to_python(self, value):
        if isinstance(value, six.string_types):
            return json.loads(value)
        return value

    def from_db_value(self, value, expression, connection, context):
        # Similar to to_python, for Django 1.8+
        if isinstance(value, six.string_types):
            return json.loads(value)
        return value

    def get_prep_value(self, value):
        if not isinstance(value, six.string_types):
            return json.dumps(value)
        return value
