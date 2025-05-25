# Algoritmo da Distância de Levenshtein

Para calcular a diferença entre duas strings, você pode usar o algoritmo da Distância de Levenshtein. Veja como você pode fazer isso:

1. Se qualquer string tiver um `length` (comprimento) de zero, retorne o `length` da outra.
2. Use um loop `for` aninhado para iterar sobre as letras das strings alvo e fonte.
3. Calcule o custo de substituição das letras correspondentes a `i - 1` e `j - 1` na string alvo e fonte, respectivamente (`0` se forem iguais, `1` caso contrário).
4. Use `Math.min()` para preencher cada elemento na matriz 2D com o mínimo da célula acima incrementada em um, da célula à esquerda incrementada em um, ou da célula superior esquerda incrementada pelo custo calculado anteriormente.
5. Retorne o último elemento da última linha da matriz produzida.

Para começar a praticar esta codificação, abra o Terminal/SSH e digite `node`. Aqui está o código que você pode usar:

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
