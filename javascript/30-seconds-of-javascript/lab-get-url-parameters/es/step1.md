# Objeto con parámetros de URL

Para crear un objeto que contenga los parámetros de la URL actual, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `String.prototype.match()` con una expresión regular adecuada para extraer todos los pares clave-valor.
3. Utilice `Array.prototype.reduce()` para mapear y combinarlos en un solo objeto.
4. Pase `location.search` como argumento para aplicarlo a la URL actual.

Aquí está el código:

```js
const getURLParameters = (url) =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => (
      (a[v.slice(0, v.indexOf("="))] = v.slice(v.indexOf("=") + 1)),
      a
    ),
    {}
  );
```

Puede utilizar esta función con cualquier URL para obtener un objeto con sus parámetros. Aquí hay algunos ejemplos:

```js
getURLParameters("google.com"); // {}
getURLParameters("http://url.com/page?name=Adam&surname=Smith");
// {name: 'Adam','surname': 'Smith'}
```
