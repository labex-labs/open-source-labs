# Calculando a Distância Entre Dois Pontos

Para calcular a distância entre dois pontos, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use `Math.hypot()` para calcular a distância euclidiana (Euclidean distance) entre dois pontos.
3.  Implemente o código abaixo, substituindo os valores `x0`, `y0`, `x1` e `y1` pelas coordenadas dos seus pontos.

```js
const distance = (x0, y0, x1, y1) => Math.hypot(x1 - x0, y1 - y0);
```

Aqui está um exemplo de como usar esta função:

```js
distance(1, 1, 2, 3); // ~2.2361
```

Isso exibirá a distância entre os pontos `(1, 1)` e `(2, 3)`.
