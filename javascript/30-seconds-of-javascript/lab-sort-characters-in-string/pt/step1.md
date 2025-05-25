# Como ordenar caracteres em uma string:

Use o seguinte código para ordenar os caracteres em uma string alfabeticamente:

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

Para começar, abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

Exemplo de uso:

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
