# Final Sigma Django Template

A django project with all of the go-to configurations for a Final Sigma application.

## Tech Stack:

- Bulma (SASS)
- Hotwire (JS)
- Stimulus (JS)

### PyPI Packages

- [django](https://pypi.org/project/Django/)
- [django-configurations](https://pypi.org/project/django-configurations/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/)
- [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
- [crispy-bulma](https://pypi.org/project/django-crispy-forms/)


## Workflow Reference

### Styles

To customize style, go to `static/main.scss` and put your styles inside the `@use "path/to/bulma/sass" with ();` list:

```sass
@use "path/to/bulma/sass" with (
  $bulma_var1: style1,
  $bulma_var2: style2,
)
```

### JavaScript

Use standard `yarn` commands from the project root directory.

- `yarn run build-css`: Updates stylesheets.
- `yarn run build-js`: Updates javascript.
- `yarn run init`: Installs dependencies and runs build scripts.
- `yarn run start`: Watches stylesheets and javascript for changes and runs django dev server.
- `yarn run build`: Manually updates both stylesheets & css.

#### Hotwire & Stimulus

Imported in `frontend/src/application/app.js`.

Stimulus controllers to be placed in `frontend/src/application/controllers/` directory.

## Packages to Configure For

- [x] python-webpack-boilerplate (w/ Turbo, Stimulus, & Bulma)
- [x] django-configurations
- [x] dj-database-url (which is built-into django-configurations)
- [x] django-debug-toolbar
- [x] django-crispy-forms and crispy-bulma
- [ ] django-allauth

## Setup to Complete

- [x] /templates directory w/ base.html (imports from webpack-boilerplate)
- [ ] inital example app with the following:
  - [ ] sample landing page
  - [ ] sample navigation bar (logo, links, dropdowns, and hamburger using stimulus)
  - [ ] sample modal (using stimulus)
  - [ ] sample form (crispy, in-place reload using turbo-frames/streams)