# Linkar arquivo CSS em HTML

Agora, precisamos linkar nosso arquivo CSS nos templates HTML. O Flask adiciona automaticamente uma view `static` que serve arquivos estáticos. Podemos usar a função `url_for` no template `base.html` para linkar nosso arquivo CSS.

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
