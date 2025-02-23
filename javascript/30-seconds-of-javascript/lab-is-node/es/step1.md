# Cómo determinar si el entorno de tiempo de ejecución actual es Node.js

Para determinar si el entorno de tiempo de ejecución actual es Node.js, siga estos pasos:

1. Abra la Terminal/SSH.
2. Escriba `node`.
3. Utilice el objeto global `process` que proporciona información sobre el proceso de Node.js actual.
4. Verifique si `process`, `process.versions` y `process.versions.node` están definidos.

Aquí está el código para determinar si el entorno de tiempo de ejecución actual es Node.js:

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

Puede probar el código llamando a la función `isNode`:

```js
isNode(); // true (Node)
isNode(); // false (navegador)
```
