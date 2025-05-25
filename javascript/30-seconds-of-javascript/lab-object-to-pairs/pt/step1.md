# Convertendo um Objeto em um Array de Pares Chave-Valor

Para converter um objeto em um array de pares chave-valor, você pode seguir estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use o método `Object.entries()` para obter um array de arrays de pares chave-valor a partir do objeto.
3. Crie uma função chamada `objectToPairs` que aceita um objeto como argumento e retorna o array de pares chave-valor.
4. Chame a função `objectToPairs` com um objeto de exemplo para testar a saída.

Aqui está um exemplo de implementação:

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

Seguindo estes passos, você pode facilmente converter um objeto em um array de pares chave-valor usando JavaScript.
