# Sub-arrays de Elementos Consecutivos

Para praticar a codificação, abra o Terminal/SSH e digite `node`. O código a seguir cria um array de `n`-tuplas de elementos consecutivos.

```js
const aperture = (n, arr) =>
  n > arr.length ? [] : arr.slice(n - 1).map((v, i) => arr.slice(i, i + n));
```

Para usar a função:

- Chame a função `aperture(n, arr)` com `n` como o número de elementos consecutivos e `arr` como o array de números.
- A função retorna um array de `n`-tuplas de elementos consecutivos de `arr`.
- Se `n` for maior que o comprimento de `arr`, a função retorna um array vazio.

Exemplo de uso:

```js
aperture(2, [1, 2, 3, 4]); // [[1, 2], [2, 3], [3, 4]]
aperture(3, [1, 2, 3, 4]); // [[1, 2, 3], [2, 3, 4]]
aperture(5, [1, 2, 3, 4]); // []
```
