# Instrucciones para el generador de ciclo

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`. A continuación, crea un generador que recorra indefinidamente la matriz dada. Aquí están los pasos:

1. Utiliza un bucle `while` no terminante que `yield` un valor cada vez que se llama a `Generator.prototype.next()`.
2. Utiliza el operador módulo (`%`) con `Array.prototype.length` para obtener el índice del siguiente valor e incrementar el contador después de cada declaración `yield`.

Aquí hay un ejemplo de la función `cycleGenerator`:

```js
const cycleGenerator = function* (arr) {
  let i = 0;
  while (true) {
    yield arr[i % arr.length];
    i++;
  }
};
```

Luego puedes usar la función de la siguiente manera:

```js
const binaryCycle = cycleGenerator([0, 1]);
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
binaryCycle.next(); // { value: 0, done: false }
binaryCycle.next(); // { value: 1, done: false }
```

Con estas instrucciones, puedes crear un generador de ciclo que recorra cualquier matriz indefinidamente.
