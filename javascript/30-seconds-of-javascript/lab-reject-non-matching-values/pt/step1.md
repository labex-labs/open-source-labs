# Filtrando Valores de Array

Para filtrar um array com base em uma função predicado e retornar apenas os valores para os quais a função predicado retorna false, siga estes passos:

1.  Use `Array.prototype.filter()` em combinação com a função predicado, `pred`.
2.  O método filter retornará apenas os valores para os quais a função predicado retorna `false`.
3.  Para rejeitar valores que não correspondem, passe a função predicado e o array para a função `reject()`.

```js
const reject = (pred, array) => array.filter((...args) => !pred(...args));
```

Aqui estão alguns exemplos de como usar a função `reject()`:

```js
reject((x) => x % 2 === 0, [1, 2, 3, 4, 5]); // [1, 3, 5]
reject((word) => word.length > 4, ["Apple", "Pear", "Kiwi", "Banana"]);
// ['Pear', 'Kiwi']
```

Seguindo estes passos, você pode facilmente filtrar um array com base em uma função predicado e rejeitar valores que não correspondem.
