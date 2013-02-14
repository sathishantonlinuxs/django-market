# -*- coding: utf-8 -*-
from django import forms

class ImageForm(forms.Form):
  imageFile = forms.ImageField(
    label='Select a file',
    help_text='max. 42 megabytes'

  )