# Currying una función

Para aplicar currying a una función, sigue estos pasos:

1. Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
2. Utiliza recursividad.
3. Verifica si la cantidad de argumentos proporcionados (`args`) es suficiente.
4. Si es así, llama a la función pasada `fn`.
5. Si no, utiliza `Function.prototype.bind()` para devolver una función curried `fn` que espera el resto de los argumentos.
6. Si quieres aplicar currying a una función que acepta un número variable de argumentos (una función variádica, por ejemplo `Math.min()`), puedes opcionalmente pasar la cantidad de argumentos al segundo parámetro `arity`.
7. Utiliza el siguiente código:

```js
const curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

Aquí hay algunos ejemplos:

```js
curry(Math.pow)(2)(10); // 1024
curry(Math.min, 3)(10)(50)(2); // 2
```
