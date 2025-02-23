# Generador de rango

Para generar un rango de valores utilizando un paso dado, utiliza la siguiente función `rangeGenerator`. Abre la Terminal/SSH y escribe `node` para comenzar a codificar.

- Utiliza un bucle `while` y `yield` para devolver cada valor, comenzando desde `start` y terminando en `end`.
- Si quieres utilizar un paso predeterminado de `1`, omite el tercer argumento.

```js
const rangeGenerator = function* (start, end, step = 1) {
  let i = start;
  while (i < end) {
    yield i;
    i += step;
  }
};
```

Aquí hay un ejemplo de cómo utilizar la función `rangeGenerator`:

```js
for (let i of rangeGenerator(6, 10)) console.log(i);
// Muestra 6, 7, 8, 9
```
