# Convertendo Radianos para Graus

Para converter um ângulo de radianos para graus, siga estes passos:

1.  Abra o Terminal/SSH e digite `node` para começar a praticar a codificação.
2.  Use a seguinte fórmula: `graus = radianos * (180 / Math.PI)`
3.  Substitua `radianos` na fórmula pelo valor que você deseja converter.
4.  O resultado estará em graus.

Aqui está um exemplo:

```js
const radsToDegrees = (rad) => (rad * 180.0) / Math.PI;
radsToDegrees(Math.PI / 2); // 90
```

Isso converterá `π/2` radianos para `90` graus.
