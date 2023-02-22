====================================
django app of an article
====================================

Anarticle uses tag, catelog, and article models to publish articles.
Support for Ariadne graphQL with pre-defined types and basic resolvers.

------------
Requirements
------------

* Python 3.11+
* django 4.0+
* pillow 9.4.0+

--------
Settings
--------

Store uploaded file with tokenize file name, default to False

* ANARTICLE_USE_TOKEN_FILENAME = True

-------------------
Django admin mixins
-------------------

Use predefined mixins to construct the admin class.

* TagAdminMixin
* CategoryAdminMixin
* ArticleAdminMixin

.. code:: python
    from django.contrib import admin

    from anarticle.models import Tag
    from anarticle.admin.mixins import TagAdminMixin


    @admin.register(Tag)
    class TagAdmin(TagAdminMixin, ModelAdmin):
        ...

---------------------------
Ariadne types and resolvers
---------------------------

Integrate predefined types and resolvers to scheme.

Requirements
------------

* ariadne 0.16.0+
* ariadne-relay 0.1.0a8+

**resolvers**

* resolve_anarticles
* resolve_anarticle_tags
* resolve_anarticle_categories

**types**

* anarticle
* anarticle_paragraph
* anarticle_tag
* anarticle_category

**graphqls**

* anarticle/graphqls/article.graphql
* anarticle/graphqls/tag.graphql
* anarticle/graphqls/category.graphql

-------
License
-------

django-anarticle is released under the terms of **Apache license**. Full details in LICENSE file.
