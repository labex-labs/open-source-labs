# Práctica de código: Iterar N veces

Para practicar la codificación, abre la Terminal/SSH y escribe `node`. Una vez que hayas hecho eso, utiliza la siguiente función para iterar sobre una función de devolución de llamada `n` veces:

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

Para usar esta función, llama a `times()` y pasa los siguientes argumentos:

- `n`: el número de veces que quieres iterar sobre la función de devolución de llamada
- `fn`: la función de devolución de llamada sobre la que quieres iterar
- `context` (opcional): el contexto que quieres usar para la función de devolución de llamada (si no se especifica, usará un objeto `undefined` o el objeto global en modo no estricto)

Aquí hay un ejemplo de cómo usar la función `times()`:

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

Esto iterará sobre la función de devolución de llamada `i => (output += i)` 5 veces y almacenará la salida en la variable `output`. Luego, la salida se registrará en la consola, lo que mostrará `01234`.
