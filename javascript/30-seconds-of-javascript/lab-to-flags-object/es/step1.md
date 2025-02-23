# Convertir una matriz en un objeto de banderas

Si quieres comenzar a practicar la programación, abre la Terminal/SSH y escribe `node`.

La siguiente función convierte una matriz de cadenas en un objeto que mapea a `true`.

Para hacer esto, usamos `Array.prototype.reduce()`. Este método convierte la matriz en un objeto, donde cada valor de la matriz sirve como una clave cuyo valor se establece en `true`.

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

Aquí hay un ejemplo:

```js
flags(["red", "green"]); // { red: true, green: true }
```
