
- Grinberg's Tutorial on [Templates](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- Jinja2 [documentation](http://jinja.pocoo.org/docs/2.10/templates/)
- Jinja2 snippets

```
{% extends 'template.html' %}
{% block content %}
    {% if task == 'content1' %}
        {% include 'content1.html' %}
    {% endif %}
    {% if task == 'content2' %}
        {% include 'content2.html' %}
    {% endif %}
{% endblock %}
```
