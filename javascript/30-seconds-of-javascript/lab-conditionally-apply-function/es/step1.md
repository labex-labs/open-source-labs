# Usando la función when para aplicar una condición

Para aplicar una función cuando se cumple una cierta condición, utiliza la función `when`. Para comenzar, abre la Terminal/SSH y escribe `node`.

La función `when` devuelve una nueva función que toma un argumento y ejecuta una devolución de llamada si el argumento es verdadero, o devuelve el argumento si es falso. La función espera un solo valor, `x`, y devuelve el valor adecuado según el parámetro `pred`.

Aquí hay una implementación de ejemplo de la función `when`:

```js
const when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

Puedes utilizar la función `when` para crear una nueva función que duplica los números pares:

```js
const doubleEvenNumbers = when(
  (x) => x % 2 === 0,
  (x) => x * 2
);
doubleEvenNumbers(2); // 4
doubleEvenNumbers(1); // 1
```
