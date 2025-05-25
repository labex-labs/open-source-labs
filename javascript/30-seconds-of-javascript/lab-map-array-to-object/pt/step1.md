# Mapeando Array para Objeto

Para mapear os valores de um array para um objeto usando uma função, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Use `Array.prototype.reduce()` para aplicar `fn` a cada elemento em `arr` e combinar os resultados em um objeto.
3. Use `el` como a chave para cada propriedade e o resultado de `fn` como o valor.

Aqui está um trecho de código de exemplo:

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

Você pode usar a função `mapObject` como mostrado neste exemplo:

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
