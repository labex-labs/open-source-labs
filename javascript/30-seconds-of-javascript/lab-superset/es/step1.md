# Función para Comprobar si un Conjunto es un Superconjunto de Otro Conjunto

Para comprobar si un conjunto es un superconjunto de otro conjunto, utiliza la función `superSet()`. Primero, abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación. Luego, sigue los siguientes pasos:

- Crea un nuevo objeto `Set` a partir de cada iterable utilizando el constructor `Set`.
- Utiliza `Array.prototype.every()` y `Set.prototype.has()` para comprobar que cada valor en la segunda iterable está contenido en la primera.
- La función devuelve `true` si la primera iterable es un superconjunto de la segunda, excluyendo los valores duplicados. En caso contrario, devuelve `false`.

```js
const superSet = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...sB].every((v) => sA.has(v));
};
```

Utiliza `superSet()` con dos conjuntos como argumentos para comprobar si un conjunto es un superconjunto de otro conjunto.

```js
superSet(new Set([1, 2, 3, 4]), new Set([1, 2])); // true
superSet(new Set([1, 2, 3, 4]), new Set([1, 5])); // false
```
