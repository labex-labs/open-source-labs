# Calculando el factorial de un número

Para calcular el factorial de un número, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice la recursividad para calcular el factorial.
3. Si `n` es menor o igual a `1`, devuelva `1`.
4. De lo contrario, devuelva el producto de `n` y el factorial de `n - 1`.
5. Si `n` es un número negativo, lance un `TypeError`.

A continuación, se muestra el código para calcular el factorial:

```js
const factorial = (n) =>
  n < 0
    ? (() => {
        throw new TypeError("Negative numbers are not allowed!");
      })()
    : n <= 1
      ? 1
      : n * factorial(n - 1);
```

Puede probar el código llamando a la función `factorial` con un número como argumento:

```js
factorial(6); // 720
```
