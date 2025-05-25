# Instruções para Contar Frequências de Valores

Para contar a frequência de valores em um array, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use o método `Array.prototype.reduce()` para mapear valores únicos para as chaves de um objeto, adicionando às chaves existentes cada vez que o mesmo valor é encontrado. Isso criará um objeto com os valores únicos do array como chaves e suas frequências como valores.
3.  O código para esta operação é o seguinte:

```js
const frequencies = (arr) =>
  arr.reduce((a, v) => {
    a[v] = a[v] ? a[v] + 1 : 1;
    return a;
  }, {});
```

4.  Para usar esta função, chame `frequencies` com o array como seu argumento. Por exemplo:

```js
frequencies(["a", "b", "a", "c", "a", "a", "b"]); // { a: 4, b: 2, c: 1 }
frequencies([..."ball"]); // { b: 1, a: 1, l: 2 }
```

Com estas instruções, você pode facilmente contar a frequência de valores em qualquer array fornecido.
