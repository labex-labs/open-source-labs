# Instruções para calcular o ponto médio entre dois pares de pontos (x, y):

Para calcular o ponto médio entre dois pares de pontos (x, y), siga estes passos:

1. Desestruture o array para obter `x1`, `y1`, `x2` e `y2`.
2. Calcule o ponto médio para cada dimensão, dividindo a soma dos dois pontos finais por `2`.

Aqui está um trecho de código de exemplo que implementa a função de cálculo do ponto médio:

```js
const midpoint = ([x1, y1], [x2, y2]) => [(x1 + x2) / 2, (y1 + y2) / 2];
```

Você pode chamar a função `midpoint` com os seguintes parâmetros para obter as coordenadas do ponto médio:

```js
midpoint([2, 2], [4, 4]); // [3, 3]
midpoint([4, 4], [6, 6]); // [5, 5]
midpoint([1, 3], [2, 4]); // [1.5, 3.5]
```

# Começando a codificar:

Para começar a praticar a codificação, siga estes passos:

1. Abra o Terminal/SSH.
2. Digite `node` para iniciar o ambiente Node.js.
