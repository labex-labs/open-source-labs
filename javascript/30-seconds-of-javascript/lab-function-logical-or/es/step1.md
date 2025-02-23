# Usando el Operador Lógico OR para Funciones

Para comenzar a practicar la programación, abre la Terminal/SSH y escribe `node`.

El operador lógico OR (`||`) se puede utilizar para comprobar si al menos una función devuelve `true` para un conjunto dado de argumentos. Para hacer esto, llama a las dos funciones con los `args` suministrados y aplica el operador lógico OR en sus resultados.

A continuación, se muestra una implementación de ejemplo de la función `either`:

```js
const either =
  (f, g) =>
  (...args) =>
    f(...args) || g(...args);
```

Y aquí hay un ejemplo de uso de la función `either` con dos funciones `isEven` e `isPositive`:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveOrEven = either(isPositive, isEven);
isPositiveOrEven(4); // true
isPositiveOrEven(3); // true
```

En este ejemplo, `isPositiveOrEven` devuelve `true` tanto para `4` como para `3` porque `isEven` devuelve `true` para `4` y `isPositive` devuelve `true` para `3`.
