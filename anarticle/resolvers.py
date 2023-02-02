"""
Copyright (c) 2014-present, aglean Inc.
"""
from ariadne import convert_kwargs_to_snake_case
from ariadne_relay import NodeObjectType
from django.db.models import Q
from django.utils import timezone

from .models import Article, Tag, Category


article = NodeObjectType('AnArticle')


@article.instance_resolver
def resolve_article_instance(id, *_):
    return Article.objects.get(id=id)


@article.field('paragraphs')
def resolve_article_paragraphs(obj, *_):
    return obj.paragraph_set.all()


@article.connection('tags')
def resolve_article_tags(obj, *_):
    return obj.tags.all()


@convert_kwargs_to_snake_case
def resolve_articles(*_,
                     is_published=True,
                     published_at=timezone.now(),
                     exclude_tags=None,
                     include_tags=None):
    queryset = Article.objects.filter(is_published__exact=is_published,
                                      published_at__lt=published_at)

    if exclude_tags is not None:
        values = [t.strip() for t in exclude_tags.split(',')]
        queryset = queryset.exclude(tags__name__in=values)

    if include_tags is not None:
        values = [t.strip() for t in include_tags.split(',')]
        queryset = queryset.filter(tags__name__in=values)

    return queryset


article_tag = NodeObjectType('ArticleTag')


@article_tag.instance_resolver
def resolve_article_tag_instance(id, *_):
    return Tag.objects.get(id=id)


@article_tag.connection('articles')
def resolve_article_tag_articles(obj, *_):
    return obj.article_set.filter(is_published=True)


@convert_kwargs_to_snake_case
def resolve_article_tags(*_,
                         name=None,
                         exclude_tags=None,
                         include_tags=None):
    queryset = Tag.objects.all()

    if name is not None:
        queryset = queryset.filter(Q(name__exact=name),
                                   Q(name__icontains=name),
                                   Q(name__istartswith=name))

    if exclude_tags is not None:
        values = [t.strip() for t in exclude_tags.split(',')]
        queryset = queryset.exclude(name__in=values)

    if include_tags is not None:
        values = [t.strip() for t in include_tags.split(',')]
        queryset = queryset.filter(name__in=values)

    return queryset


def resolve_article(*_, slug):
    return Article.objects.get(slug=slug)

types = [article,
         article_tag]
