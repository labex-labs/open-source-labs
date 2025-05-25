# Instruções para Encontrar a Interseção de Arrays Mapeados

Para encontrar elementos comuns em dois arrays após aplicar uma função a cada elemento de ambos os arrays, siga estes passos:

1. Abra o Terminal/SSH e digite `node`.
2. Use o código fornecido abaixo:

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. No código, substitua `a` e `b` pelos seus arrays e `fn` pela função que você deseja aplicar a cada elemento.
4. Execute o código para obter o array resultante com os elementos comuns.

Exemplo:

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

No primeiro exemplo, a função `Math.floor` é aplicada aos arrays `[2.1, 1.2]` e `[2.3, 3.4]`, retornando o elemento comum `[2.1]`.
No segundo exemplo, a função `x => x.title` é aplicada aos arrays `[{ title: 'Apple' }, { title: 'Orange' }]` e `[{ title: 'Orange' }, { title: 'Melon' }]`, retornando o elemento comum `[{ title: 'Orange' }]`.
