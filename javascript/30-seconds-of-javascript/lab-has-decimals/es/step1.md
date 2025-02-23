# Cómo comprobar si un número tiene dígitos decimales

Para comprobar si un número tiene dígitos decimales, puedes utilizar el operador módulo en JavaScript. Sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza el operador módulo (`%`) para comprobar si el número es divisible por `1`.
3. Si el resultado no es igual a cero, entonces el número tiene dígitos decimales.

Aquí hay un código de ejemplo para comprobar si un número tiene dígitos decimales:

```js
const hasDecimals = (num) => num % 1 !== 0;
```

Puedes probar la función llamándola con diferentes números, como esto:

```js
hasDecimals(1); // false
hasDecimals(1.001); // true
```
