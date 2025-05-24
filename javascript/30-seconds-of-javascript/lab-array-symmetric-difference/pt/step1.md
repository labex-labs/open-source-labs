# Diferença Simétrica de Arrays

Para encontrar a diferença simétrica entre dois arrays e incluir valores duplicados, siga estes passos:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2. Crie um `Set` a partir de cada array para obter os valores únicos de cada um.
3. Use `Array.prototype.filter()` em cada um deles para manter apenas os valores que não estão contidos no outro.

Aqui está o código:

```js
const symmetricDifference = (a, b) => {
  const sA = new Set(a),
    sB = new Set(b);
  return [...a.filter((x) => !sB.has(x)), ...b.filter((x) => !sA.has(x))];
};
```

Você pode usar os seguintes exemplos para testar a função:

```js
symmetricDifference([1, 2, 3], [1, 2, 4]); // [3, 4]
symmetricDifference([1, 2, 2], [1, 3, 1]); // [2, 2, 3]
```
