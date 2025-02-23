# Agregando una imagen de fondo

A continuación, crearemos un subdirectorio para las imágenes. Crea un subdirectorio `images` en el directorio `polls/static/polls/`. Dentro de este directorio, agrega cualquier archivo de imagen que desees usar como fondo. Con fines de este tutorial, estamos usando un archivo llamado `background.png`, que puedes encontrar en el directorio `/tmp/background.png` en la VM.

Necesitas copiar el `/tmp/background.png` a `polls/static/polls/images/background.png`.

Luego, agrega una referencia a tu imagen en tu hoja de estilos (`polls/static/polls/style.css`):

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

Recarga la pestaña **Web 8080** y deberías ver que el fondo se ha cargado en la esquina superior izquierda de la pantalla.

![background image example](../assets/20230908-15-39-41-8dGms0NM.png)

> La etiqueta de plantilla `{% static %}` no está disponible para su uso en archivos estáticos que no son generados por Django, como tu hoja de estilos. Debes siempre usar **rutas relativas** para enlazar tus archivos estáticos entre sí, porque entonces puedes cambiar `STATIC_URL` (utilizado por la etiqueta de plantilla `static` para generar sus URLs) sin tener que modificar un montón de rutas en tus archivos estáticos también.

Estos son los **conceptos básicos**. Para obtener más detalles sobre la configuración y otros aspectos incluidos en el framework, consulta `the static files howto </howto/static-files/index>` y `the staticfiles reference </ref/contrib/staticfiles>`. `Deploying static files </howto/static-files/deployment>` discute cómo usar archivos estáticos en un servidor real.

Cuando te sientas cómodo con los archivos estáticos, lee **Customizing Django's Admin Site** para aprender cómo personalizar el sitio de administración automáticamente generado por Django.
