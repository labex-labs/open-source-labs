# Cómo componer funciones en JavaScript

Para comenzar a practicar la codificación utilizando la composición de funciones en JavaScript, abre la Terminal/SSH y escribe `node`.

Aquí hay un ejemplo de cómo realizar la composición de funciones de derecha a izquierda en JavaScript:

1. Utiliza `Array.prototype.reduce()` para realizar la composición de funciones de derecha a izquierda.
2. La última (más a la derecha) función puede aceptar uno o más argumentos; el resto de las funciones deben ser unarias.
3. Define la función `compose` que tomará cualquier número de funciones como argumentos y devolverá una nueva función que las componga.
4. Llama a la función `compose` con las funciones deseadas en el orden deseado.
5. Llama a la nueva función compuesta con cualquier argumento necesario.

```js
const compose = (...fns) =>
  fns.reduce(
    (f, g) =>
      (...args) =>
        f(g(...args))
  );
```

Por ejemplo, digamos que tenemos dos funciones:

```js
const add5 = (x) => x + 5;
const multiply = (x, y) => x * y;
```

Podemos componer estas funciones utilizando `compose`:

```js
const multiplyAndAdd5 = compose(add5, multiply);
```

Ahora podemos llamar a `multiplyAndAdd5` con los argumentos deseados:

```js
multiplyAndAdd5(5, 2); // 15
```
