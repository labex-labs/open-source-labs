# Crear una función con un contexto dado

Para crear una función con un contexto dado, utiliza la función `bind`. Primero, abre la Terminal/SSH y escribe `node`.

La función `bind` crea una nueva función que invoca la función original con un contexto dado. También puede opcionalmente agregar cualquier parámetro adicional suministrado a los argumentos.

Para utilizar `bind`, pasa la función original (`fn`) y el contexto deseado (`context`). También puedes pasar cualquier parámetro adicional que debe estar vinculado a la función (`...boundArgs`).

La función `bind` devuelve una nueva función que utiliza `Function.prototype.apply()` para aplicar el contexto dado a `fn`. También utiliza el operador de propagación (`...`) para agregar cualquier parámetro adicional suministrado a los argumentos.

A continuación, se muestra un ejemplo de uso de `bind`:

```js
const bind =
  (fn, context, ...boundArgs) =>
  (...args) =>
    fn.apply(context, [...boundArgs, ...args]);

function greet(greeting, punctuation) {
  return greeting + " " + this.user + punctuation;
}

const freddy = { user: "fred" };
const freddyBound = bind(greet, freddy);
console.log(freddyBound("hi", "!")); // 'hi fred!'
```

En este ejemplo, definimos una función `greet` que toma dos parámetros (`greeting` y `punctuation`) y devuelve una cadena que concatena el `greeting`, la propiedad `user` del contexto actual (`this`) y la `punctuation`.

Luego creamos un nuevo objeto (`freddy`) que tiene una propiedad `user` establecida en `'fred'`.

Finalmente, creamos una nueva función (`freddyBound`) utilizando `bind`, pasando la función `greet` y el objeto `freddy` como el contexto deseado. Luego podemos llamar a `freddyBound` con dos parámetros adicionales (`'hi'` y `'!'`), que se transmiten a la función original `greet` junto con el contexto `freddy` vinculado. La salida resultante es `'hi fred!'`.
