# Presentando el Administrador de Django

Generar sitios de administración para su personal o clientes para agregar, cambiar y eliminar contenido es un trabajo tedioso que no requiere mucha creatividad. Por esa razón, Django automatiza por completo la creación de interfaces de administración para los modelos.

Django fue escrito en un entorno de redacción, con una clara separación entre "editores de contenido" y el sitio "público". Los administradores del sitio usan el sistema para agregar noticias, eventos, puntuaciones deportivas, etc., y ese contenido se muestra en el sitio público. Django resuelve el problema de crear una interfaz unificada para que los administradores del sitio editen el contenido.

El administrador no está destinado a ser utilizado por los visitantes del sitio. Es para los administradores del sitio.

## Creando un usuario administrador

Primero necesitaremos crear un usuario que pueda iniciar sesión en el sitio de administración. Ejecute el siguiente comando:

```bash
python manage.py createsuperuser
```

Ingrese el nombre de usuario deseado y presione Enter.

```plaintext
Nombre de usuario: admin
```

Luego se le solicitará su dirección de correo electrónico deseada:

```plaintext
Dirección de correo electrónico: admin@example.com
```

El último paso es ingresar su contraseña. Se le pedirá que ingrese su contraseña dos veces, la segunda vez como confirmación de la primera.

```plaintext
Contraseña: 12345678
Contraseña (nuevamente): 12345678

Esta contraseña es muy común.
Esta contraseña es completamente numérica.
¿Saltar la validación de contraseña y crear el usuario de todos modos? [y/N]: y
Superusuario creado con éxito.
```

## Iniciar el servidor de desarrollo

El sitio de administración de Django está activado por defecto. Vamos a iniciar el servidor de desarrollo y explorarlo.

Si el servidor no está en ejecución, inícielo así:

```bash
python manage.py runserver
```

Ahora, abra un navegador web en la pestaña **VNC** y vaya a "/admin/" en su dominio local, por ejemplo, `http://127.0.0.1:8000/admin/`. Debería ver la pantalla de inicio de sesión del administrador:

![Pantalla de inicio de sesión del administrador de Django](../assets/20230907-14-31-50-SvkJF8K8.png)

Dado que `la traducción </topics/i18n/translation>` está activada por defecto, si establece `LANGUAGE_CODE`, la pantalla de inicio de sesión se mostrará en el idioma dado (si Django tiene las traducciones adecuadas).

## Ingresar al sitio de administración

Ahora, intente iniciar sesión con la cuenta de superusuario que creó en el paso anterior. Debería ver la página de índice del administrador de Django:

![Página de índice del administrador de Django](../assets/admin02.png)

Debería ver algunos tipos de contenido editable: grupos y usuarios. Son proporcionados por `django.contrib.auth`, el marco de autenticación que viene con Django.

## Hacer que la aplicación de sondeo sea modificable en el administrador

Pero, ¿dónde está nuestra aplicación de sondeo? No se muestra en la página de índice del administrador.

Solo queda una cosa por hacer: tenemos que decirle al administrador que los objetos `Question` tienen una interfaz de administración. Para hacer esto, abra el archivo `polls/admin.py` y edítelo para que se vea así:

```python
from django.contrib import admin

from.models import Question

admin.site.register(Question)
```

## Explorar la funcionalidad de administración gratuita

Ahora que hemos registrado `Question`, Django sabe que debe mostrarse en la página de índice del administrador:

![Página de índice del administrador de Django, ahora con sondeos mostrados](../assets/admin03t.png)

Haga clic en "Preguntas". Ahora estás en la página de "lista de cambios" para las preguntas. Esta página muestra todas las preguntas en la base de datos y te permite elegir una para cambiarla. Allí está la pregunta "¿Qué pasa?" que creamos anteriormente:

![Página de lista de cambios de sondeos](../assets/admin04t.png)

Haga clic en la pregunta "¿Qué pasa?" para editarla:

![Editando una pregunta de sondeo](../assets/20230907-14-33-49-XWeEgAXl.png)

Cosas que hay que notar aquí:

- El formulario se genera automáticamente a partir del modelo `Question`.
- Los diferentes tipos de campos de modelo (`~django.db.models.DateTimeField`, `~django.db.models.CharField`) corresponden al widget de entrada HTML adecuado. Cada tipo de campo sabe cómo mostrarse en el administrador de Django.
- Cada `~django.db.models.DateTimeField` obtiene atajos de JavaScript gratuitos. Las fechas obtienen un atajo "Hoy" y un desplegable de calendario, y las horas obtienen un atajo "Ahora" y un desplegable conveniente que lista las horas comúnmente ingresadas.

La parte inferior de la página te da un par de opciones:

- Guardar -- Guarda los cambios y regresa a la página de lista de cambios para este tipo de objeto.
- Guardar y continuar editando -- Guarda los cambios y recarga la página de administrador para este objeto.
- Guardar y agregar otro -- Guarda los cambios y carga un nuevo formulario en blanco para este tipo de objeto.
- Eliminar -- Muestra una página de confirmación de eliminación.

Si el valor de "Fecha publicada" no coincide con la hora en que creó la pregunta en **Creación de una Aplicación Básica de Sondeo**, probablemente significa que olvidó establecer el valor correcto para la configuración `TIME_ZONE`. Cambielo, recargue la página y verifique que aparezca el valor correcto.

Cambie la "Fecha publicada" haciendo clic en los atajos "Hoy" y "Ahora". Luego haga clic en "Guardar y continuar editando". Luego haga clic en "Historial" en la esquina superior derecha. Verá una página que lista todos los cambios realizados a este objeto a través del administrador de Django, con la marca de tiempo y el nombre de usuario de la persona que hizo el cambio:

![Página de historial del objeto de pregunta](../assets/admin06t.png)

Cuando esté cómodo con la API de modelos y se haya familiarizado con el sitio de administración, lea **Creando las Vistas de la Interfaz Pública** para aprender cómo agregar más vistas a nuestra aplicación de sondeos.
