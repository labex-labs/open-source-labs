# Función para elegir las propiedades de un objeto que coinciden con una condición dada

Para elegir las propiedades de un objeto que coinciden con una condición dada, utiliza la función `pickBy()`. Esta función crea un nuevo objeto compuesto por las propiedades para las cuales la función dada devuelve un valor verdadero.

- Utiliza `Object.keys()` y `Array.prototype.filter()` para eliminar las propiedades para las cuales `fn` devuelve un valor falso.
- Utiliza `Array.prototype.reduce()` para convertir las propiedades filtradas de nuevo en un objeto con los correspondientes pares clave-valor.
- La función de devolución de llamada se invoca con dos argumentos: (valor, clave).

Aquí está el código de la función `pickBy()`:

```js
const pickBy = (obj, fn) =>
  Object.keys(obj)
    .filter((k) => fn(obj[k], k))
    .reduce((acc, key) => ((acc[key] = obj[key]), acc), {});
```

Puedes utilizar esta función para elegir las propiedades que coinciden con una condición. Por ejemplo:

```js
pickBy({ a: 1, b: "2", c: 3 }, (x) => typeof x === "number");
// { 'a': 1, 'c': 3 }
```
