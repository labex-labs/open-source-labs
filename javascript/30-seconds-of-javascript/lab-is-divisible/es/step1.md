# Comprobar si un número es divisible

Para comprobar si un número es divisible por otro número en JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Utilice el operador módulo (`%`) para comprobar si el resto de la división es igual a `0`. Si es así, entonces el número es divisible.

A continuación, se muestra una función de ejemplo que comprueba si el primer argumento numérico es divisible por el segundo:

```js
const isDivisible = (dividend, divisor) => dividend % divisor === 0;
```

Puede probar esta función con `isDivisible(6, 3)`, que debería devolver `true` ya que 6 es divisible por 3.
