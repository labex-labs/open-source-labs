# Cómo obtener un array sin el último elemento

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Aquí te mostramos cómo devolver todos los elementos de un array excepto el último:

- Utiliza `Array.prototype.slice()` para devolver todos los elementos del array excepto el último.

```js
const initial = (arr) => arr.slice(0, -1);
```

Aquí tienes un ejemplo:

```js
initial([1, 2, 3]); // [1, 2]
```
