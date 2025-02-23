# Unión y normalización de segmentos de URL

Para unir los segmentos de URL dados y normalizar la URL resultante, siga los pasos siguientes:

1. Utilice `Array.prototype.join()` para combinar los segmentos de URL.
2. Utilice una serie de llamadas a `String.prototype.replace()` con diferentes expresiones regulares para normalizar la URL resultante:
   - Eliminando barras dobles
   - Agregando barras adecuadas para el protocolo
   - Eliminando barras antes de los parámetros
   - Combinando parámetros con `'&'` y normalizando el primer delimitador de parámetros.

Utilice el fragmento de código siguiente para unir y normalizar los segmentos de URL:

```js
const URLJoin = (...args) =>
  args
    .join("/")
    .replace(/[\/]+/g, "/")
    .replace(/^(.+):\//, "$1://")
    .replace(/^file:/, "file:/")
    .replace(/\/(\?|&|#[^!])/g, "$1")
    .replace(/\?/g, "&")
    .replace("&", "?");
```

Uso de ejemplo:

```js
URLJoin("http://www.google.com", "a", "/b/cd", "?foo=123", "?bar=foo");
// 'http://www.google.com/a/b/cd?foo=123&bar=foo'
```
