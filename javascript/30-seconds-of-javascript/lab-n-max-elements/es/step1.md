# Cómo obtener los n elementos máximos de una matriz en JavaScript

Para practicar la programación en JavaScript, abre la Terminal/SSH y escribe `node`. Una vez que hayas hecho eso, puedes usar los siguientes pasos para obtener los `n` elementos máximos de una matriz:

1. Utiliza `Array.prototype.sort()` junto con el operador de propagación (`...`) para crear una clonación superficial de la matriz y ordenarla en orden descendente.
2. Utiliza `Array.prototype.slice()` para obtener el número especificado de elementos.
3. Si omites el segundo argumento, `n`, obtendrás una matriz de un solo elemento por defecto.
4. Si `n` es mayor o igual que la longitud de la matriz proporcionada, entonces devuelve la matriz original (ordenada en orden descendente).

Aquí está el código JavaScript para la función `maxN` que implementa estos pasos:

```js
const maxN = (arr, n = 1) => [...arr].sort((a, b) => b - a).slice(0, n);
```

Puedes probar la función `maxN` con los siguientes ejemplos:

```js
maxN([1, 2, 3]); // [3]
maxN([1, 2, 3], 2); // [3, 2]
```
