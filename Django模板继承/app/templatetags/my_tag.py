from django import template
from django.utils.safestring import mark_safe

# register是固定变量名，不能改变
register = template.Library()

@register.simple_tag
def my_add100(val, val_2):
  return val + 100 + val_2
