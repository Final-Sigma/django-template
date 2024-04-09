# Final Sigma Django Template

A django project with all of the go-to configurations for a Final Sigma application.

## Tech Stack:

- Bulma (SASS)
- Hotwire (JS)
- Stimulus (JS)

### PyPI Packages

- [django](https://pypi.org/project/Django/)
- [python-webpack-boilerplate](https://pypi.org/project/python-webpack-boilerplate/)
- [django-configurations](https://pypi.org/project/django-configurations/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/)
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
- [crispy-bulma](https://pypi.org/project/django-crispy-forms/)


## Workflow Reference

### Styles

To customize style, go to `frontend/src/styles/index.scss` and put your styles inside the `@use "bulma/sass" with ();` list:

```sass
@use "bulma/sass" with (
  $bulma_var1: style1,
  $bulma_var2: style2,
)
```

### JavaScript

Use standard `npm` commands from the project root directory.

#### Hotwire & Stimulus

Imported in `frontend/src/application/app.js`.

Stimulus controllers to be placed in `frontend/src/application/controllers/` directory.

## Packages to Configure For

- [ ] python-webpack-boilerplate (w/ Turbo, Stimulus, & Bulma)
- [ ] django-configurations
- [ ] dj-database-url (which is built-into django-configurations)
- [ ] django-debug-toolbar
- [ ] django-crispy-forms and crispy-bulma
- [ ] django-allauth

## Setup to Complete

- [ ] /templates directory w/ base.html (imports from webpack-boilerplate)
- [ ] inital example app with the following:
  - [ ] sample landing page
  - [ ] sample navigation bar (logo, links, dropdowns, and hamburger using stimulus)
  - [ ] sample modal (using stimulus)
  - [ ] sample form (crispy, in-place reload using turbo-frames/streams)