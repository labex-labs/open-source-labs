# Usando el AND Lógico con Funciones

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.

Para comprobar si dos funciones devuelven `true` para un conjunto dado de argumentos, utiliza el operador lógico AND (`&&`).

```js
const both =
  (f, g) =>
  (...args) =>
    f(...args) && g(...args);
```

El código anterior crea una nueva función `both` que toma dos funciones `f` y `g` como entrada y devuelve otra función que llama a `f` y `g` con los argumentos suministrados y devuelve `true` solo si ambas funciones devuelven `true`.

Por ejemplo, para comprobar si un número es positivo y par, podemos usar las funciones `isEven` y `isPositive` con `both` como se muestra a continuación:

```js
const isEven = (num) => num % 2 === 0;
const isPositive = (num) => num > 0;
const isPositiveEven = both(isEven, isPositive);
isPositiveEven(4); // true
isPositiveEven(-2); // false
```

Aquí, `isPositiveEven` es una nueva función que comprueba si un número dado es positivo y par al usar la función `both` con `isEven` e `isPositive` como entradas.
