# Función de JavaScript para analizar cookies HTTP

Para analizar una cadena de encabezado de cookie HTTP en JavaScript y devolver un objeto con todos los pares nombre-valor de cookies, siga estos pasos:

- Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
- Utilice `String.prototype.split()` para separar los pares clave-valor entre sí.
- Utilice `Array.prototype.map()` y `String.prototype.split()` para separar las claves de los valores en cada par.
- Utilice `Array.prototype.reduce()` y `decodeURIComponent()` para crear un objeto con todos los pares clave-valor.

A continuación, se muestra un ejemplo de la función `parseCookie()` que implementa los pasos anteriores:

```js
const parseCookie = (str) =>
  str
    .split(";")
    .map((v) => v.split("="))
    .reduce((acc, v) => {
      acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
      return acc;
    }, {});
```

Puede probar la función de la siguiente manera:

```js
parseCookie("foo=bar; equation=E%3Dmc%5E2");
// { foo: 'bar', equation: 'E=mc^2' }
```
