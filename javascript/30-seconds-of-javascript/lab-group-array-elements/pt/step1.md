# Agrupar Elementos de Arrays

Para agrupar elementos de arrays com base em suas posições nos arrays originais, use a função `zip` fornecida abaixo.

- Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
- A função `zip` usa `Math.max()` e `Function.prototype.apply()` para obter o array mais longo nos argumentos.
- Ela cria um array com esse comprimento como valor de retorno e usa `Array.from()` com uma função de mapeamento para criar um array de elementos agrupados.
- Se os comprimentos dos arrays de argumentos variarem, `undefined` é usado onde nenhum valor pôde ser encontrado.

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

Exemplo de uso:

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
