# Convertir una cadena de consulta en un objeto

Para convertir una cadena de consulta o URL en un objeto, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice `String.prototype.split()` para extraer los parámetros de la `url` dada.
3. Utilice el constructor `URLSearchParams` para crear un objeto y conviértalo en una matriz de pares clave-valor utilizando el operador de propagación (`...`).
4. Utilice `Array.prototype.reduce()` para convertir la matriz de pares clave-valor en un objeto.

A continuación, se muestra el código para convertir la cadena de consulta:

```js
const queryStringToObject = (url) =>
  [...new URLSearchParams(url.split("?")[1])].reduce(
    (a, [k, v]) => ((a[k] = v), a),
    {}
  );
```

Uso de ejemplo:

```js
queryStringToObject("https://google.com?page=1&count=10");
// {page: '1', count: '10'}
```
