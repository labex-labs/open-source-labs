# Promesas en JavaScript

Para comprobar si un objeto es similar a una Promesa, utiliza la función `isPromiseLike`. Esta función verifica si el objeto no es nulo, tiene un tipo de objeto o función y tiene una propiedad `.then` que también es una función.

Aquí está el código para `isPromiseLike`:

```js
const isPromiseLike = (obj) =>
  obj !== null &&
  (typeof obj === "object" || typeof obj === "function") &&
  typeof obj.then === "function";
```

Aquí hay algunos ejemplos de cómo usar `isPromiseLike`:

```js
isPromiseLike({
  then: function () {
    return "";
  }
}); // true

isPromiseLike(null); // false

isPromiseLike({}); // false
```

Para comenzar a practicar la codificación en JavaScript, abre la Terminal/SSH y escribe `node`.
