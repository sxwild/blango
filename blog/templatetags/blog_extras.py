from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django import template

user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, user=None):
  if isinstance(author, user_model):
    if isinstance(user, user_model) and author.username == user.username:
      name = format_html("<b>Me</b>")
    elif author.first_name and author.last_name:
      name = f'{author.first_name} {author.last_name}'
    else:
      name = author.username
    if author.email and author.username != user.username:
      email = author.email
      name = format_html('<a href="mailto:{}">{}</a>', email, name)
  else:
    name = ""

  return name
