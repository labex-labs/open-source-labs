# Diferença Simétrica de Array Mapeado

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Esta função retorna a diferença simétrica (symmetric difference) entre dois arrays, após aplicar a função fornecida a cada elemento de ambos os arrays. Veja como funciona:

- Crie um `Set` a partir de cada array para obter os valores únicos de cada um após aplicar `fn` a eles.
- Use `Array.prototype.filter()` em cada um deles para manter apenas os valores que não estão contidos no outro.

Aqui está o código para a função `symmetricDifferenceBy`:

```js
const symmetricDifferenceBy = (a, b, fn) => {
  const sA = new Set(a.map((v) => fn(v))),
    sB = new Set(b.map((v) => fn(v)));
  return [
    ...a.filter((x) => !sB.has(fn(x))),
    ...b.filter((x) => !sA.has(fn(x)))
  ];
};
```

Você pode usar `symmetricDifferenceBy` assim:

```js
symmetricDifferenceBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [ 1.2, 3.4 ]
symmetricDifferenceBy(
  [{ id: 1 }, { id: 2 }, { id: 3 }],
  [{ id: 1 }, { id: 2 }, { id: 4 }],
  (i) => i.id
);
// [{ id: 3 }, { id: 4 }]
```
