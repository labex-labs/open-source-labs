# Convertendo um Iterável para um Hash

Para converter um iterável (objeto ou array) em um hash (armazenamento de dados indexado), siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Object.values()` para obter os valores do iterável.
3. Use `Array.prototype.reduce()` para iterar sobre os valores e criar um objeto que é indexado pelo valor de referência.
4. Chame a função `toHash` com o iterável e um parâmetro de chave opcional para especificar o valor de referência.

Aqui está um exemplo de implementação da função `toHash` em JavaScript:

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

Você pode chamar a função `toHash` com diferentes iteráveis e chaves para criar diferentes hashes. Por exemplo:

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
