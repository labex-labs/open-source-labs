# Convertendo um Array em um Objeto com Base em uma Chave Específica

Para converter um array em um objeto com base em uma chave específica e excluir essa chave de cada valor, siga estas etapas:

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- Use `Array.prototype.reduce()` para criar um objeto a partir do array fornecido.
- Use a desestruturação de objetos para extrair o valor da `key` fornecida e os `data` associados, e então adicione o par chave-valor ao objeto.

Aqui está um exemplo de implementação:

```js
const indexOn = (arr, key) =>
  arr.reduce((obj, v) => {
    const { [key]: id, ...data } = v;
    obj[id] = data;
    return obj;
  }, {});
```

Você pode então usar a função assim:

```js
indexOn(
  [
    { id: 10, name: "apple" },
    { id: 20, name: "orange" }
  ],
  "id"
);
// { '10': { name: 'apple' }, '20': { name: 'orange' } }
```
