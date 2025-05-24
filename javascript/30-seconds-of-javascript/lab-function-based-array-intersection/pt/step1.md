# Como Encontrar a Interseção de Arrays com Base em uma Função Usando JavaScript

Para encontrar os elementos que existem em ambos os arrays com base em uma função comparadora fornecida, siga estas etapas:

1. Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.

2. Use `Array.prototype.filter()` e `Array.prototype.findIndex()` em combinação com o comparador fornecido para determinar os valores de interseção.

   ```js
   const intersectionWith = (a, b, comp) =>
     a.filter((x) => b.findIndex((y) => comp(x, y)) !== -1);
   ```

3. Chame a função `intersectionWith()` com os dois arrays e a função comparadora como argumentos.

   ```js
   intersectionWith(
     [1, 1.2, 1.5, 3, 0],
     [1.9, 3, 0, 3.9],
     (a, b) => Math.round(a) === Math.round(b)
   ); // [1.5, 3, 0]
   ```

Isso retornará um array contendo os valores de interseção entre os dois arrays, com base na função comparadora fornecida.
