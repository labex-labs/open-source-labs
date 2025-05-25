# Função para Combinar Arrays com uma Função de Mapeamento Fornecida

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Esta função retorna um array de elementos que existem em qualquer um dos dois arrays de entrada, após aplicar a função de mapeamento fornecida a cada elemento em ambos os arrays.

Aqui estão os passos para alcançar isso:

1.  Crie um novo `Set` (conjunto) aplicando a função de mapeamento a todos os valores no primeiro array de entrada `a`.
2.  Crie outro `Set` consistindo em todos os elementos em `b` que não correspondem a nenhum valor no `Set` criado anteriormente quando a função de mapeamento é aplicada.
3.  Combine os dois conjuntos e converta-os em um array.
4.  Retorne o array resultante.

Aqui está o código para a função `unionBy`:

```js
const unionBy = (a, b, fn) => {
  const setA = new Set(a.map(fn));
  return Array.from(new Set([...a, ...b.filter((x) => !setA.has(fn(x)))]));
};
```

Aqui estão alguns exemplos de como usar a função `unionBy`:

```js
unionBy([2.1], [1.2, 2.3], Math.floor); // Output: [2.1, 1.2]
unionBy([{ id: 1 }, { id: 2 }], [{ id: 2 }, { id: 3 }], (x) => x.id);
// Output: [{ id: 1 }, { id: 2 }, { id: 3 }]
```
