# Busca de Substring _Case-Insensitive_

Para verificar se uma string contém uma substring, independentemente da capitalização, siga estes passos:

- Use o construtor `RegExp` com a flag `'i'` para criar uma expressão regular que corresponda à `searchString` fornecida, ignorando a capitalização.
- Use `RegExp.prototype.test()` para verificar se a string contém a substring.

Aqui está um exemplo de trecho de código:

```js
const includesCaseInsensitive = (str, searchString) =>
  new RegExp(searchString, "i").test(str);
```

Para testar esta função, você pode executar:

```js
includesCaseInsensitive("Blue Whale", "blue"); // true
```
