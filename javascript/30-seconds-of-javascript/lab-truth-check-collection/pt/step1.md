# Função de Verificação de Verdade em Coleção

Para praticar a codificação, digite `node` no Terminal/SSH.

Aqui está uma função que verifica se uma função predicado é verdadeira para todos os elementos de uma coleção.

- Use `Array.prototype.every()` para verificar se cada objeto passado possui a propriedade especificada e se ela retorna um valor verdadeiro (truthy).

```js
const truthCheckCollection = (collection, pre) =>
  collection.every((obj) => obj[pre]);
```

Exemplo de uso:

```js
truthCheckCollection(
  [
    { user: "Tinky-Winky", sex: "male" },
    { user: "Dipsy", sex: "male" }
  ],
  "sex"
); // true
```
