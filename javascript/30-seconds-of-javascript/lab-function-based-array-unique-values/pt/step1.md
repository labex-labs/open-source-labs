# Encontrando Valores Únicos em um Array com uma Função

Para encontrar todos os valores únicos de um array, forneça uma função comparadora.

Use `Array.prototype.reduce()` e `Array.prototype.some()` para criar um array contendo apenas a primeira ocorrência única de cada valor. A função comparadora `fn` recebe dois argumentos, os valores dos dois elementos que estão sendo comparados.

```js
const uniqueElementsBy = (arr, fn) =>
  arr.reduce((acc, v) => {
    if (!acc.some((x) => fn(v, x))) acc.push(v);
    return acc;
  }, []);
```

Para testar a função, use o exemplo abaixo:

```js
uniqueElementsBy(
  [
    { id: 0, value: "a" },
    { id: 1, value: "b" },
    { id: 2, value: "c" },
    { id: 1, value: "d" },
    { id: 0, value: "e" }
  ],
  (a, b) => a.id == b.id
); // [ { id: 0, value: 'a' }, { id: 1, value: 'b' }, { id: 2, value: 'c' } ]
```

Comece a praticar a codificação abrindo o Terminal/SSH e digitando `node`.
