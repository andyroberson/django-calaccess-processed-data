#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OCD Jurisdiction-related models and managers.

Copied (with some modifications) from
https://github.com/opencivicdata/python-opencivicdata-django/blob/master/opencivicdata/models/jurisdiction.py
"""
from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.encoding import python_2_unicode_compatible
from calaccess_processed.models.base import CalAccessBaseModel
from .common import JURISDICTION_CLASSIFICATION_CHOICES, SESSION_CLASSIFICATION_CHOICES
from .base import OCDBase, OCDIDField, RelatedBase
from .division import Division


@python_2_unicode_compatible
class Jurisdiction(CalAccessBaseModel, OCDBase):
    """
    OCD Jurisdiction model, as defined in OCDEP 3: Jurisdictions.
    """
    id = OCDIDField(ocd_type='jurisdiction')
    name = models.CharField(max_length=300)
    url = models.URLField(max_length=2000)
    classification = models.CharField(max_length=50, choices=JURISDICTION_CLASSIFICATION_CHOICES,
                                      default='government', db_index=True)
    feature_flags = ArrayField(base_field=models.TextField(), blank=True, default=list)
    division = models.ForeignKey(Division, related_name='jurisdictions', db_index=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class LegislativeSession(CalAccessBaseModel, RelatedBase):
    """
    OCD LegislativeSession model, as defined in OCDEP 3: Jurisdictions.
    """
    jurisdiction = models.ForeignKey(Jurisdiction, related_name='legislative_sessions')
    identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    classification = models.CharField(max_length=100, choices=SESSION_CLASSIFICATION_CHOICES,
                                      blank=True)
    start_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]
    end_date = models.CharField(max_length=10)    # YYYY[-MM[-DD]]

    def __str__(self):
        return '{} {}'.format(self.jurisdiction, self.name)