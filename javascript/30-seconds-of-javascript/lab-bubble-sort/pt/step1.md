# Algoritmo Bubble Sort (Ordenação por Bolha)

Para praticar a codificação, abra o Terminal/SSH e digite `node` para iniciar. O algoritmo bubble sort (ordenação por bolha) ordena um array de números.

Passos para ordenar um array usando o algoritmo bubble sort:

1.  Declare uma variável, `swapped` (trocado), que indica se algum valor foi trocado durante a iteração atual.

2.  Use o operador spread (`...`) para clonar o array original, `arr`.

3.  Use um loop `for` para iterar sobre os elementos do array clonado, terminando antes do último elemento.

4.  Use um loop `for` aninhado para iterar sobre o segmento do array entre `0` e `i`, trocando quaisquer elementos adjacentes fora de ordem e definindo `swapped` como `true`.

5.  Se `swapped` for `false` após uma iteração, nenhuma outra alteração é necessária, então o array clonado é retornado.

Exemplo de código:

```js
const bubbleSort = (arr) => {
  let swapped = false;
  const a = [...arr];
  for (let i = 1; i < a.length; i++) {
    swapped = false;
    for (let j = 0; j < a.length - i; j++) {
      if (a[j + 1] < a[j]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        swapped = true;
      }
    }
    if (!swapped) return a;
  }
  return a;
};

bubbleSort([2, 1, 4, 3]); // [1, 2, 3, 4]
```
