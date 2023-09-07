# Installing Django Debug Toolbar

Django Debug Toolbar is a useful tool for debugging Django web applications. It's a third-party package maintained by the [Jazzband](https://jazzband.co) organization. The toolbar helps you understand how your application functions and to identify problems. It does so by providing panels that provide debug information about the current request and response.

To install a third-party application like the toolbar, you need to install the package by running the below command within an activated virtual environment. This is similar to our earlier step to `install Django
<installing-official-release>`.

```bash
python -m pip install django-debug-toolbar
```

Third-party packages that integrate with Django need some post-installation setup to integrate them with your project. Often you will need to add the package's Django app to your `INSTALLED_APPS` setting. Some packages need other changes, like additions to your URLconf (`urls.py`).

Django Debug Toolbar requires several setup steps. Follow them in [its installation guide](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html). The steps are not duplicated in this tutorial, because as a third-party package, it may change separately to Django's schedule.

Once installed, you should be able to see the DjDT "handle" on the right side of the browser window when you refresh the polls application. Click it to open the debug toolbar and use the tools in each panel. See the [panels documentation page](https://django-debug-toolbar.readthedocs.io/en/latest/panels.html) for more information on what the panels show.
