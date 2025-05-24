# Diferença de Arrays

Para encontrar a diferença entre dois arrays, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a codificar.

2.  Crie um `Set` a partir do array `b` para extrair os valores únicos de `b`.

3.  Use `Array.prototype.filter()` no array `a` para manter apenas os valores que não estão no array `b`, usando `Set.prototype.has()`.

Aqui está o código:

```js
const difference = (a, b) => {
  const s = new Set(b);
  return a.filter((x) => !s.has(x));
};
```

Exemplo de uso:

```js
difference([1, 2, 3, 3], [1, 2, 4]); // Output: [3, 3]
```
