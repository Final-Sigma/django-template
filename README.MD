# Django Template

A project by [Final Sigma](https://finalsigma.io).

## Rationale

Isn't starting a new project exhausting? Shouldn't it be easier to get up and running, to eliminate as much friction as possible when you have a new idea.

This template solves a problem that I have personally run into over the years. I have always enjoyed working in Django. I have not always liked tracking down and installing all the third-party packages I need to get a Django project started.

Here I have tried to collect all of the third-party packages I typically reach for and build a rudimentary example application to both demonstrate and document their implementation. This project is the fruit of many hours of [yak shaving](http://www.catb.org/~esr/jargon/html/Y/yak-shaving.html).

As I discover better ways to do and accomplish different features, I hope to return to this template and implement what I've learned, making it a repository of my own preferences and best practices.

Feel free to explore, use it on your own projects, and provide me feedback. It's [MIT Licensed](https://en.wikipedia.org/wiki/MIT_License) for a reason. Please don't hesitate to provide feedback (and pull requests!) as I'm always looking to learn and improve.

## Tech Stack

Below I'll outline the core technologies utilized in creating this project template.

### Yarn

I've chosen Yarn for managing npm packages. This project will require you to have Yarn and NodeJS installed globally on your system. I've included several scripts in `package.json`, but the main ones are:

#### `$ yarn run build-css`

Uses [sass](https://www.npmjs.com/package/sass) to compile stylesheets from `assets/css/index.scss` and deposit the result in `static/app.css` & `static/app.css.map`.

#### `$ yarn run build-js`

Uses [webpack](https://www.npmjs.com/package/webpack) to compile JavaScript from `assets/js/index.js` and deposit the result in `static/app.js`.

### Bulma

This project utilizes [Bulma](https://bulma.io) as its CSS library. This template includes some [basic customization](https://bulma.io/documentation/customize/with-sass/).

To implement custom variables, modify the following in `assets/css/index.scss`:

```scss
// assets/css/index.scss

@use '../node_modules/bulma/sass' with (
    $primary: rgb(0, 175, 0),
    // additional variables here
);

// import fonts *after* initializing Bulma
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Micro+5+Charted&display=swap')
```

### Turbo

I *do not* want to write any more JavaScript than is absolutely necessary. So I've implemented [@hotwired/turbo](https://www.npmjs.com/package/@hotwired/turbo) as the front-end JavaScript library.

With links that use redirects to take a user to a page hosted outside your domain and back (like [Stripe Checkout](https://docs.stripe.com/payments/checkout)), you will need to write the link/button with `data-turbo=false` to temporarily disable Turbo for that interaction.

```django
<form method='post'>
  {% csrf_token %}
  {{ form }}
  <button type="submit" data-turbo="false">
    Go to Strip Checkout
  </button>
</form>
```

The basics work out of the box (which is one reason I love Turbo), and additional documentation can be found in the [Turbo Handbook](https://turbo.hotwired.dev/).

### Stimulus

This project uses [Stimulus]([django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/)) to provide interactive components to the user interface. Stimulus controllers will be auto-detected in the `assets/js/controllers/` directory. A full tutorial can be found in the [Stiumulus Handbook](https://stimulus.hotwired.dev/handbook/origin).

### Summernote (WYSIWYG Editor)

This template includes the [Summernote](https://summernote.org/) WYSIWYG editor, implemented through the [django-summernote](https://github.com/summernote/django-summernote) package.

You will find an example of its usage in how the included example blog handles the body of a blog post:

```python
# example_blog/models.py

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(
        max_length=50
    )
    # ...
```

```python
# example_blog/forms.py

from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from .models import BlogPost as Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'body': SummernoteWidget() # <= Loads Summer Note when this
        }                              #    form is called in a template. 
```

```python
# example_blog/views.py

from django.views.generic.edit import CreateView, UpdateView
from .forms import PostForm
from .models import BlogPost as Post

# ...

class PostsCreate(CreateView):
    model = Post
    form_class = PostForm      # <= Loads the above-mentioned form
                               #    which includes the Summernote widget.
class PostsUpdate(UpdateView):
    model = Post
    form_class = PostForm      # <= In both views.

# ...
```

```django
{# example_blog/templates/example_blog/blogpost_form.html #}

{% extends 'example_blog/base.html' %}

{% block content %}
<form method="post"
      action="{% if object %}{% url 'blog:edit_post' object.pk %}{% else %}{% url 'blog:new_post' %}{% endif %}"
>
{% csrf_token %}
{{ form }} {# <= Will use the Summernote widget declared in blog_example/forms.py #}
<input type="submit" class="button is-primary"
value=
    {%if object %}
    "Update Post"
    {% else %}
    "Create Post"
    {% endif %}
> 
</form>
{% endblock %}

{# Since this single template is responsible to produce #}
{# the form for both creating a new blog post and       #}
{# editing an existing one, there is logic to change    #}
{# form action and button text accordingly.             #}
```

### Crispy Forms

Forms use the [crispy forms](https://github.com/django-crispy-forms/django-crispy-forms) package for styling and the [crispy bulma](https://github.com/ckrybus/crispy-bulma) template package. In the latest version, the crispy form helper is not working.

### Django Configurations

TODO: Write documenation on [django-configurations](https://pypi.org/project/django-configurations/)

### Django Database URL

TODO: Write documenation on [dj-database-url](https://pypi.org/project/dj-database-url/)

### Django Debug Toolbar

TODO: Write documentation on [django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/)

## Workflow Paradigms

TODO: Write about creating a new app

TODO: Write about creating CRUD resource in that app.

TODO: Write about adding resource to Sitemap.

TODO: Write about adding pagination to an IndexView.

TODO: Write about modifying Django Admin with custom admin site.