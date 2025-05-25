# Como Determinar se o Ambiente de Tempo de Execução Atual é Node.js

Para determinar se o ambiente de tempo de execução atual é Node.js, siga estes passos:

1. Abra o Terminal/SSH.
2. Digite `node`.
3. Use o objeto global `process` que fornece informações sobre o processo Node.js atual.
4. Verifique se `process`, `process.versions` e `process.versions.node` estão definidos.

Aqui está o código para determinar se o ambiente de tempo de execução atual é Node.js:

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

Você pode testar o código chamando a função `isNode`:

```js
isNode(); // true (Node)
isNode(); // false (browser)
```
