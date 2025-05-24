# Cálculo da Distância Euclidiana

Para calcular a distância entre dois pontos em qualquer número de dimensões, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Object.keys()` e `Array.prototype.map()` para mapear cada coordenada para a sua diferença entre os dois pontos.
3.  Use `Math.hypot()` para calcular a distância Euclidiana (Euclidean distance) entre os dois pontos.

Aqui está um trecho de código de exemplo para ajudá-lo a começar:

```js
const euclideanDistance = (a, b) =>
  Math.hypot(...Object.keys(a).map((k) => b[k] - a[k]));
```

Você pode testar a função usando estas entradas de exemplo:

```js
euclideanDistance([1, 1], [2, 3]); // ~2.2361
euclideanDistance([1, 1, 1], [2, 3, 2]); // ~2.4495
```
