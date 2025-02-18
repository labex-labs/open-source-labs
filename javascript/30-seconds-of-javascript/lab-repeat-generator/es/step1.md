# Práctica de código con el Generador de repetición

Para practicar la codificación, abre la Terminal/SSH y escribe `node` para crear un generador que repita el valor dado indefinidamente. Utiliza un bucle `while` sin finalización que `yield` (proporcione) un valor cada vez que se llame a `Generator.prototype.next()`. Luego, utiliza el valor de retorno de la declaración `yield` para actualizar el valor devuelto si el valor pasado no es `undefined`.

```js
const repeatGenerator = function* (val) {
  let v = val;
  while (true) {
    let newV = yield v;
    if (newV !== undefined) v = newV;
  }
};
```

Para probar el generador, crea una instancia de él utilizando el valor `5` y llama a `repeater.next()` para obtener el siguiente valor de la secuencia. La salida será `{ value: 5, done: false }`. Llamar a `repeater.next()` de nuevo devolverá el mismo valor. Para cambiar el valor, llama a `repeater.next(4)`, lo que devolverá `{ value: 4, done: false }`. Finalmente, llamar a `repeater.next()` devolverá el valor actualizado, `{ value: 4, done: false }`.
