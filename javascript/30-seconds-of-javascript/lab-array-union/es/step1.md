# Cómo encontrar la unión de dos arrays en JavaScript

Para encontrar la unión de dos arrays en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.

2. La unión de dos arrays devuelve cada elemento que existe en cualquiera de los dos arrays al menos una vez.

3. Para obtener la unión de dos arrays, cree un `Set` con todos los valores de `a` y `b`, y conviértalo en un array utilizando el método `Array.from()`.

A continuación, se muestra un ejemplo de cómo implementar esto:

```js
const union = (a, b) => Array.from(new Set([...a, ...b]));

console.log(union([1, 2, 3], [4, 3, 2])); // Salida: [1, 2, 3, 4]
```

En el ejemplo anterior, la función `union()` toma dos arrays, `[1, 2, 3]` y `[4, 3, 2]`, como argumentos y devuelve la unión de los dos arrays como un array `[1, 2, 3, 4]`.
