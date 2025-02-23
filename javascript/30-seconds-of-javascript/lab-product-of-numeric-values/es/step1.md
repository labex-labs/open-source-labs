# Cómo calcular el producto de valores numéricos en JavaScript

Para calcular el producto de dos o más números o arrays en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el método `Array.prototype.reduce()` para multiplicar cada valor por un acumulador, que debe inicializarse con un valor de `1`.
3. Defina una función llamada `prod` que tome cualquier número de argumentos utilizando el operador de propagación (`...`). Dentro de la función, aplique el método `reduce()` al array de argumentos expandido.
4. La función devuelve el resultado de la multiplicación.

A continuación, se muestra un ejemplo de cómo utilizar la función `prod`:

```js
const prod = (...arr) => [...arr].reduce((acc, val) => acc * val, 1);

prod(1, 2, 3, 4); // 24
prod(...[1, 2, 3, 4]); // 24
```

En el ejemplo anterior, `prod(1, 2, 3, 4)` y `prod(...[1, 2, 3, 4])` ambos devuelven `24`.
