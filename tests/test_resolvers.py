"""
Copyright (c) 2014-present, aglean Inc.
"""
import pytest

from anarticle.resolvers import resolve_anarticle_tags, \
        resolve_anarticle_categories, resolve_anarticles


@pytest.mark.django_db
def test_reoslve_tags_from_root_without_args():
    assert resolve_anarticle_tags(None, None).count() == 0


@pytest.mark.django_db
def test_reoslve_tags_from_root_with_args():
    assert resolve_anarticle_tags(None, None, name='test').count() == 0


def test_resolve_tags_from_obj_without_args(mocker):
    queryset = mocker.patch('anarticle.models.Tag.objects.all')
    queryset.return_value = queryset
    queryset.count.return_value = 1
    assert resolve_anarticle_tags(queryset, None).count() == 1


def test_resolve_tags_from_obj_with_args(mocker):
    queryset = mocker.patch('anarticle.models.Tag.objects.filter')
    queryset.return_value = queryset
    queryset.count.return_value = 1
    assert resolve_anarticle_tags(queryset, None, name='test').count() == 1


@pytest.mark.django_db
def test_reoslve_categories_from_root_without_args():
    assert resolve_anarticle_categories(None, None).count() == 0


@pytest.mark.django_db
def test_reoslve_categories_from_root_with_args():
    assert resolve_anarticle_categories(None,
                                        None,
                                        name='test',
                                        description='test').count() == 0


def test_resolve_categories_from_obj_without_args(mocker):
    queryset = mocker.patch('anarticle.models.Category.objects.all')
    queryset.return_value = queryset
    queryset.count.return_value = 0
    assert resolve_anarticle_categories(queryset, None).count() == 0


def test_resolve_categories_from_obj_with_args(mocker):
    queryset = mocker.patch('anarticle.models.Category.objects.filter')
    queryset.return_value = queryset
    queryset.count.return_value = 0
    assert resolve_anarticle_categories(queryset,
                                        None,
                                        name='test',
                                        description='test').count() == 0


@pytest.mark.django_db
def test_reoslve_articles_from_root_without_args():
    assert resolve_anarticles(None, None).count() == 0


@pytest.mark.django_db
def test_reoslve_articles_from_root_with_args():
    assert resolve_anarticles(None, None, name='test,value').count() == 0


def test_resolve_articles_from_obj_without_args(mocker):
    queryset = mocker.patch('anarticle.models.Article.objects.filter')
    queryset.return_value = queryset
    queryset.count.return_value = 2
    assert resolve_anarticles(queryset, None).count() == 2


def test_resolve_articles_from_obj_with_args(mocker):
    queryset = mocker.patch('anarticle.models.Article.objects.filter')
    queryset.return_value = queryset
    queryset.count.return_value = 2
    assert resolve_anarticles(queryset, None, name='test,value').count() == 2
