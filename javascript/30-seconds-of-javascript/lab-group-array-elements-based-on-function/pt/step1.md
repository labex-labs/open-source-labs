# Função JavaScript para Agrupar Elementos de Array

Para agrupar elementos em arrays, você pode usar a função `zipWith`.

Veja como funciona:

- A função recebe um número ilimitado de arrays como argumentos.
- Ela verifica se o último argumento é uma função.
- Ela usa `Math.max()` para encontrar o comprimento do array mais longo.
- Ela cria um novo array de elementos agrupados usando `Array.from()` e uma função de mapeamento.
- Se os comprimentos dos arrays de argumentos variarem, `undefined` é usado onde nenhum valor pôde ser encontrado.
- A função é invocada com os elementos de cada grupo.

Aqui está um exemplo de uso da função `zipWith`:

```js
zipWith([1, 2], [10, 20], [100, 200], (a, b, c) => a + b + c); // [111, 222]
zipWith(
  [1, 2, 3],
  [10, 20],
  [100, 200],
  (a, b, c) =>
    (a != null ? a : "a") + (b != null ? b : "b") + (c != null ? c : "c")
); // [111, 222, '3bc']
```

Para usar a função `zipWith`, abra o Terminal/SSH e digite `node`.
