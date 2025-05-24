# Convertendo Valores para Arrays em JavaScript

Para converter um valor em um array, use a função `castArray` fornecida abaixo.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

Para usar esta função, passe o valor que você deseja converter como argumento. A função verificará se o valor já é um array usando `Array.isArray()`. Se for um array, a função o retornará como está. Se não for um array, a função retornará o valor encapsulado em um array.

Aqui está um exemplo de como usar `castArray`:

```js
castArray("foo"); // returns: ['foo']
castArray([1]); // returns: [1]
```

Para começar a praticar a codificação em JavaScript, abra o Terminal ou SSH e digite `node`.
