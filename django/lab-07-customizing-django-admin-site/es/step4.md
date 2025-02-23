# Personalizar la apariencia y sensación del administrador

Obviamente, tener "Administración de Django" en la parte superior de cada página de administración es ridículo. Es solo texto de marcador de posición.

Sin embargo, puede cambiarlo usando el sistema de plantillas de Django. La interfaz de administración de Django está impulsada por Django mismo, y sus interfaces utilizan el propio sistema de plantillas de Django.

## Personalizando las plantillas de su _proyecto_

Cree un directorio `templates` en el directorio de su proyecto (el que contiene `manage.py`). Las plantillas pueden estar en cualquier lugar del sistema de archivos que Django pueda acceder. (Django se ejecuta como el usuario que ejecute su servidor.) Sin embargo, mantener sus plantillas dentro del proyecto es una buena convención que seguir.

Abra su archivo de configuración (`mysite/settings.py`, recuerde) y agregue una opción `DIRS <TEMPLATES-DIRS>` en la configuración `TEMPLATES`:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

`DIRS <TEMPLATES-DIRS>` es una lista de directorios del sistema de archivos para verificar cuando se cargan las plantillas de Django; es una ruta de búsqueda.

## Organizando las plantillas

Al igual que los archivos estáticos, _podríamos_ tener todas nuestras plantillas juntas, en un gran directorio de plantillas, y funcionaría perfectamente. Sin embargo, las plantillas que pertenecen a una aplicación en particular deben ubicarse en el directorio de plantillas de esa aplicación (por ejemplo, `polls/templates`) en lugar del del proyecto (`templates`). Vamos a discutir en más detalle en el tutorial de `aplicaciones reutilizables </intro/reusable-apps>` _por qué_ hacemos esto.

Ahora cree un directorio llamado `admin` dentro de `templates`, y copie la plantilla `admin/base_site.html` desde dentro del directorio de plantillas de administración predeterminado de Django en el código fuente de Django mismo (`django/contrib/admin/templates`) en ese directorio.

## ¿Dónde están los archivos fuente de Django?

Si tiene dificultades para encontrar donde se encuentran los archivos fuente de Django en su sistema, ejecute el siguiente comando:

```bash
python -c "import django; print(django.__path__)"
```

```plaintext
['/home/labex/.local/lib/python3.10/site-packages/django']
```

Luego, edite el archivo y reemplace `{{ site_header|default:_('Django administration') }}` (incluyendo las llaves) con el nombre de su propio sitio según le parezca adecuado. Debería terminar con una sección de código como:

```html+django
{% block branding %}
<div id="site-name"><a href="{% url 'admin:index' %}">Administración de Encuestas</a><div>
{% endblock %}
```

Usamos este enfoque para enseñarle cómo sobrescribir plantillas. En un proyecto real, probablemente usaría el atributo `django.contrib.admin.AdminSite.site_header` para hacer esta personalización en particular de manera más fácil.

Este archivo de plantilla contiene mucho texto como `{% block branding %}` y `{{ title }}`. Las etiquetas `{%` y `{{` son parte del lenguaje de plantillas de Django. Cuando Django renderiza `admin/base_site.html`, este lenguaje de plantillas se evaluará para producir la página HTML final, al igual que vimos en `**Creando las vistas de la interfaz pública**`.

Tenga en cuenta que cualquiera de las plantillas de administración predeterminadas de Django se puede sobrescribir. Para sobrescribir una plantilla, haga lo mismo que hizo con `base_site.html`: cópiela del directorio predeterminado en su directorio personalizado y haga los cambios.

## Personalizando las plantillas de su _aplicación_

Los lectores perspicaces se preguntarán: Pero si `DIRS <TEMPLATES-DIRS>` estaba vacío por defecto, ¿cómo estaba Django encontrando las plantillas de administración predeterminadas? La respuesta es que, dado que `APP_DIRS <TEMPLATES-APP_DIRS>` está establecido en `True`, Django busca automáticamente un subdirectorio `templates/` dentro de cada paquete de aplicación, para usarlo como alternativa (no olvide que `django.contrib.admin` es una aplicación).

Nuestra aplicación de encuestas no es muy compleja y no necesita plantillas de administración personalizadas. Pero si se volviera más sofisticada y requiriera la modificación de las plantillas de administración estándar de Django para alguna de sus funcionalidades, sería más sensato modificar las plantillas de la _aplicación_, en lugar de las del _proyecto_. De esa manera, podría incluir la aplicación de encuestas en cualquier nuevo proyecto y estar seguro de que encontraría las plantillas personalizadas que necesitaba.

Consulte la `documentación de carga de plantillas <template-loading>` para obtener más información sobre cómo Django encuentra sus plantillas.
