# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    link_text = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField(auto_now_add=True)
    user_email = models.EmailField(max_length=200, default="")

    def __str__(self):
        return self.link_text
