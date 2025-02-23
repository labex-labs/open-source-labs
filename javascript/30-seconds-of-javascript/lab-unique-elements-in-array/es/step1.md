# Cómo encontrar valores únicos en un array con JavaScript

Para encontrar todos los valores únicos en un array, puedes seguir estos pasos en JavaScript:

1. Crea un `Set` a partir del array dado para descartar los valores duplicados.
2. Utiliza el operador de propagación (`...`) para convertir el `Set` de nuevo en un array.

Aquí hay un fragmento de código de ejemplo:

```js
const getUniqueValues = (arr) => [...new Set(arr)];
```

Puedes llamar a la función y pasarle un array, como esto:

```js
getUniqueValues([1, 2, 2, 3, 4, 4, 5]); // [1, 2, 3, 4, 5]
```

Esto devolverá un array con todos los valores únicos del array original, sin ningún duplicado.
