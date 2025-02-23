# XOR Lógico

Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`. El xor lógico verifica si solo uno de los argumentos es `true`. Para crear el xor lógico, utiliza los operadores lógicos o (`||`), y (`&&`) y no (`!`) en los dos valores dados. Aquí te presento un código de ejemplo para ello:

```js
const xor = (a, b) => (a || b) && !(a && b);
```

A continuación se presentan los valores de salida:

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
