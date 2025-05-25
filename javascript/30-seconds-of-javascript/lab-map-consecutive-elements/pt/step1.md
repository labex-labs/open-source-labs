# Função para Mapear Elementos Consecutivos em um Array

Para começar a codificar, abra o Terminal/SSH e digite `node`.

Esta função mapeia cada bloco de `n` elementos consecutivos em um array, usando a função fornecida `fn`. Siga estes passos:

- Use `Array.prototype.slice()` para obter um novo array `arr` com os primeiros `n` elementos removidos.
- Use `Array.prototype.map()` e `Array.prototype.slice()` para aplicar `fn` a cada bloco de `n` elementos consecutivos em `arr`.

Aqui está o código:

```js
const mapConsecutive = (arr, n, fn) =>
  arr.slice(n - 1).map((v, i) => fn(arr.slice(i, i + n)));
```

Por exemplo, você pode usar `mapConsecutive()` para mapear cada bloco de 3 elementos consecutivos em um array de números, juntando-os com traços:

```js
mapConsecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, (x) => x.join("-"));
// ['1-2-3', '2-3-4', '3-4-5', '4-5-6', '5-6-7', '6-7-8', '7-8-9', '8-9-10'];
```
