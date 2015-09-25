# -*- coding:utf-8 -*-
from django.test import TestCase

from testapp.models import JSONModel


class TestSaveLoad(TestCase):

    def test_empty_dict(self):
        m = JSONModel()
        assert m.attrs == {}
        m.save()
        m = JSONModel.objects.get()
        assert m.attrs == {}

    def test_values(self):
        m = JSONModel(attrs={'key': 'value'})
        assert m.attrs == {'key': 'value'}
        m.save()
        m = JSONModel.objects.get()
        assert m.attrs == {'key': 'value'}

    def test_list(self):
        m = JSONModel(attrs=[1, 2, 4])
        assert m.attrs == [1, 2, 4]
        m.save()
        m = JSONModel.objects.get()
        assert m.attrs == [1, 2, 4]
