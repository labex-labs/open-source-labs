# Include Necessary Files

The setuptools build backend needs another file named `MANIFEST.in` to include non-Python files in the project.

Create a `MANIFEST.in` with the following content:

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

This tells the build to copy everything in the `static` and `templates` directories, and the `schema.sql` file, while excluding all bytecode files.
