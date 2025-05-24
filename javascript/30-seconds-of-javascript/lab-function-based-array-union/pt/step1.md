# Como Encontrar a União de Dois Arrays com Base em uma Função

Para encontrar a união de dois arrays com base em uma função usando Node.js, siga estes passos:

1. Abra o Terminal/SSH e digite `node`.
2. Use o seguinte código para criar um `Set` com todos os valores de `a` e os valores em `b` para os quais o comparador não encontra correspondências em `a`, usando `Array.prototype.findIndex()`:

```js
const unionWith = (a, b, comp) =>
  Array.from(
    new Set([...a, ...b.filter((x) => a.findIndex((y) => comp(x, y)) === -1)])
  );
```

3. Chame a função `unionWith` com três argumentos: o primeiro array, o segundo array e a função comparadora.
4. A função retorna cada elemento que existe em qualquer um dos dois arrays pelo menos uma vez, usando a função comparadora fornecida.
5. Aqui está um exemplo de como chamar a função `unionWith`:

```js
unionWith(
  [1, 1.2, 1.5, 3, 0],
  [1.9, 3, 0, 3.9],
  (a, b) => Math.round(a) === Math.round(b)
);
// [1, 1.2, 1.5, 3, 0, 3.9]
```

Isso retornará `[1, 1.2, 1.5, 3, 0, 3.9]` como a união dos dois arrays.
