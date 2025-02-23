# Comprobando si un subconjunto de un iterable está contenido en otro iterable

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Esta función comprueba si el primer iterable es un subconjunto del segundo iterable, excluyendo valores duplicados.

Para lograr esto, puedes hacer lo siguiente:

- Crea un nuevo objeto `Set` a partir de cada iterable utilizando el constructor `Set`.
- Utiliza `Array.prototype.every()` y `Set.prototype.has()` para comprobar si cada valor en el primer iterable está contenido en el segundo iterable.

A continuación, se muestra una implementación de ejemplo:

```js
const subSet = (a, b) => {
  const setA = new Set(a);
  const setB = new Set(b);
  return [...setA].every((value) => setB.has(value));
};
```

Puedes utilizar la función `subSet` pasando dos conjuntos para comparar. Por ejemplo:

```js
subSet(new Set([1, 2]), new Set([1, 2, 3, 4])); // true
subSet(new Set([1, 5]), new Set([1, 2, 3, 4])); // false
```
