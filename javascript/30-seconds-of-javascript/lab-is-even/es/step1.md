# Comprobar si un número es par

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Utiliza el siguiente código para comprobar si un número es par o impar:

```js
const isEven = (num) => num % 2 === 0;
```

El código anterior utiliza el operador módulo (`%`) para comprobar si un número es impar o par. Si el número es par, la función devuelve `true`. Si es impar, la función devuelve `false`.

A continuación, se muestra un ejemplo de cómo utilizar la función `isEven`:

```js
isEven(3); // devuelve false
```
