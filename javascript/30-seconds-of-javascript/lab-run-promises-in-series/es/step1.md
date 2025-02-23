# Ejecutando Promesas en Serie

Para ejecutar una matriz de promesas en serie, utiliza `Array.prototype.reduce()` para crear una cadena de promesas. Cada promesa devuelve la siguiente promesa después de ser resuelta.

Para comenzar, abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.

Aquí hay un ejemplo del código:

```js
const runPromisesInSeries = (ps) =>
  ps.reduce((p, next) => p.then(next), Promise.resolve());
```

Luego, puedes utilizar la función `runPromisesInSeries` para ejecutar las promesas secuencialmente, como se muestra en el siguiente ejemplo:

```js
const delay = (d) => new Promise((r) => setTimeout(r, d));
runPromisesInSeries([() => delay(1000), () => delay(2000)]);
// Este código ejecuta cada promesa secuencialmente, tardando un total de 3 segundos en completarse.
```
