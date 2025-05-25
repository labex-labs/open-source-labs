# Convertendo Array para Objeto de Flags

Se você deseja começar a praticar a codificação, abra o Terminal/SSH e digite `node`.

A seguinte função converte um array de strings em um objeto que mapeia para true.

Para fazer isso, usamos `Array.prototype.reduce()`. Este método converte o array em um objeto, onde cada valor do array serve como uma chave cujo valor é definido como `true`.

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

Aqui está um exemplo:

```js
flags(["red", "green"]); // { red: true, green: true }
```
