# Vincular el archivo CSS en HTML

Ahora, necesitamos vincular nuestro archivo CSS en las plantillas HTML. Flask agrega automáticamente una vista `static` que sirve archivos estáticos. Podemos usar la función `url_for` en la plantilla `base.html` para vincular nuestro archivo CSS.

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
