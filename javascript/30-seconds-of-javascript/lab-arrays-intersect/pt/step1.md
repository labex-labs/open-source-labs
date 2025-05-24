# Como Verificar se Dois Arrays Possuem um Item em Comum

Para verificar se dois arrays possuem um item em comum, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Crie um `Set` a partir de `b` para obter os valores únicos em `b`.
3.  Use `Array.prototype.some()` em `a` para verificar se algum de seus valores está contido em `b`, usando `Set.prototype.has()`.
4.  Use a função `intersects` fornecida abaixo para testar os arrays.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

Use a função `intersects` para verificar se dois arrays se intersectam:

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

Seguindo estes passos e usando o código fornecido, você pode facilmente verificar se dois arrays possuem um item em comum.
